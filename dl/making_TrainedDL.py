#DL코드
import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, LSTM, Layer, Activation
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.preprocessing.sequence import pad_sequences#문장 패딩해주는 애
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#vocab_size = len(self.vocab2idx) + 1
excel_address='/content/drive/MyDrive/융소_ossp_수강추천시스템DL/OSSProj_DL_sign-up-course/sample_classes.xlsx'
class Recommend_LSTM(tf.keras.Model):
  def __init__(self, vocab_size,embedding_matrix , hidden_size=16, embedding_dimension=8):
    super(Recommend_LSTM, self).__init__()
    self.embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dimension,weights=[embedding_matrix])
    self.lstm = LSTM(units=hidden_size, return_sequences=True, return_state=True)
    self.dense = Dense(units=vocab_size, activation="softmax")

  def call(self, encoded_classes_list, training=False):
    X = self.embedding_layer(encoded_classes_list)
    X, _, _ = self.lstm(X)
    X = self.dense(X)
    return X

  def set_vocab(self,vocab_size,vocab2idx,idx2vocab):
    self.vocab_size=vocab_size
    self.vocab2idx=vocab2idx
    self.idx2vocab=idx2vocab

  def get_config(self):
    config = {
       'vocab_size': self.vocab_size,
       'embedding_matrix': self.embedding_layer.get_weights()[0].tolist(),
       'hidden_size': self.lstm.units,
       'embedding_dimension': self.embedding_layer.output_dim,
       'vocab2idx':self.vocab2idx,
       'idx2vocab':self.idx2vocab,
       'lstm_weights':self.lstm.get_weights(),
       'dense_weights':self.dense.get_weights()
        }
    base_config = super(Recommend_LSTM, self).get_config()
    return dict(list(base_config.items()) + list(config.items()))

  @classmethod
  def from_config(cls, config):
    model = cls(
       vocab_size=config['vocab_size'],
       embedding_matrix=np.array(config['embedding_matrix']),
       hidden_size=config['hidden_size'],
       embedding_dimension=config['embedding_dimension'],
       vocab2idx = config['vocab2idx'],
       idx2vocab = config['idx2vocab'],
       lstm_weights = config['lstm_weights'],
       dense_weights = config['dense_weights']
        )


  class Node():
    def __init__(self, word, probability, prev_node, next_nodes, num_layer):
      self.word = word
      if num_layer==0 or type(prev_node) == list or type(prev_node) == type(None):#self.head는 num_layer=0, prev_node=None임 / self.tail만 self.tail.prev_node를 list로 하여 노드 객체 리스트로 여러 노드를 저장하기 때문 -> 이 if문은 현재 생성되는 노드가 head or tail임을 검사한다.
        #print("현재 생성되는 노드는 head or tail이다.")
        self.probability = -tf.math.log(probability)
        #print("{}의 probability : {}, -tf.math.log(probability) : {},누적확률 : {}".format(self.word,probability,-tf.math.log(probability),self.probability))

      else:#실제 과목을 저장하고 있는 노드
        self.probability=prev_node.probability-tf.math.log(probability)
      self.prev_node = prev_node
      self.next_nodes = next_nodes#이 노드 객체의 word로부터 딥러닝 모델을 거처 예상된 k개의 후보 단어들을 저장할 각각의 노드들로, list에 노드들이 각각 들어갈 것임
      self.num_layer = num_layer#이 노드가 몇 번째 layer에 있는지 의미(int임)

  def BeamSearch(self,taken_classes,num_class=10,beam_size=2):
    self.head = self.Node(word="head",probability=1.0,prev_node=None,next_nodes=None,num_layer=0);self.tail=self.Node("tail",1.0,prev_node=list([]),next_nodes=None,num_layer=num_class)
    self.head.next_nodes=self.tail
    #첫번째 예측 단어들의 확률 계산
    self.num_class=num_class
    taken_classes = taken_classes[0]
    encoded_data = [[self.vocab2idx[word] for word in taken_classes]]
    encoded_data = tf.constant(encoded_data)
    #print("정수 인코딩된 기수강 과목들(encoded_data)의 shape = \n",encoded_data.shape)#(2차원 텐서(즉 행렬)여야 한다! -> 그래야 embedding_layer지나면, 3차원이 되어 lstm을 문제없이 지나니까)
    X = self.embedding_layer(encoded_data)
    #print("lstm 입력될 텐서 shape(X) = ",X.shape)
    hidden_states, last_hidden_state, last_cell_state = self.lstm(X)
    initial_state = [last_hidden_state, last_cell_state]
    probabilities = self.dense(last_hidden_state)
    #print("last_hidden_state의 shape = (1,vocab_size+1)이어야됨. \n",last_hidden_state.shape)
    probabilities = tf.squeeze(probabilities)
    #가장 확률 큰 beamsize개의 예측 단어 찾아 각각 노드에 저장 and head와 연결
    sorted_indices = tf.argsort(probabilities,axis=0,direction="DESCENDING")
    top_k_indices = sorted_indices[:beam_size]
    top_k_indices = top_k_indices.numpy().tolist()
    #print(top_k_indices)

    words = [self.idx2vocab[index] for index in top_k_indices]#첫번째 예상 단어 후보 리스트
    #print("첫번째 예상 단어 후보 리스트 : ",words)
    probabilities_of_words = [probabilities[index] for index in top_k_indices]
    #print("첫번째 예상 단어 후보 각각에 대응되는 확률 리스트: ",probabilities_of_words)
    #노드에 저장 및 head와 연결
    words_nodes = self.insert(words,probabilities_of_words,self.head,num_layer=1)

    #print("word_nodes = ",words_nodes)
    #각 첫번째 예측 단어 후보들(words_nodes들의 원소(노드)들)로부터 똑같이 후보 예측 and 현재 노드(words_nodes의 원소)에 연결
    i=0
    for word_node in words_nodes:
      i+=1
      #print("{}번 째".format(i))
      #print("word_node = ",word_node)
      self.predict(word_node,initial_state,beam_size)

    #후보 path(추천 과목 모음)들 찾기(num_path만큼)
    sentences = self.search_max_prob_nodes(self.tail,num_path=1)

    #예측까지 다 했으면, self.head, self.tail 초기화
    self.head = self.Node(word="head",probability=1.0,prev_node=None,next_nodes=None,num_layer=0);self.tail=self.Node("tail",1.0,prev_node=list([]),next_nodes=None,num_layer=self.num_class)
    self.head.next_nodes=self.tail
    return sentences

  def insert(self,next_words,probabilities,present_node,num_layer):#next_words들 각각을 저장하는 노드를 만들어 present_node에 연결(가장 끝 layer의 노드들(지금 present_node 뒤에 오는 단어 노드들)은 self.tail에 연결)
    #여기서 input으로 주어진 num_layer := 이제 만들어질 노드들의 계층
    present_node.next_nodes = list([])
    #end 토큰 검사
    for word in next_words:
      if word=="<end>":
        end_index = next_words.index("<end>")
        del next_words[end_index];del probabilities[end_index]
        if present_node not in self.tail.prev_node:#present_node 다음에 end가 후보에 있으면, 이 end 토큰 뒤엔 단어 예측 필요x 즉, present_node의 단어가 마지막 단어로 예상되니, present_node와 tail 연결
          self.tail.prev_node.append(present_node)#tail.prev_node에는 각 path의 마지막 노드만 저장하도록 하기!
        break #한 번 단어 예측할 때마다 end는 next_words 중 최대 단 한 개만 존재(dense layer에서 각 단어 개수 만큼 크기의 확률벡터(각 단어에 한 개씩 대응)를 return하니) -> end 토큰 찾았으면, 더 이상 for문 필요 x
    #pad 토큰 겁사
    for word in next_words:
      if word=="<pad>":
        pad_index = next_words.index("<pad>")
        del next_words[pad_index];del probabilities[pad_index]
        if present_node not in self.tail.prev_node:#present_node 다음에 end가 후보에 있으면, 이 end 토큰 뒤엔 단어 예측 필요x 즉, present_node의 단어가 마지막 단어로 예상되니, present_node와 tail 연결
          self.tail.prev_node.append(present_node)
    #next_words, probabilities에서 end, pad 모두 빼고, 나머지 단어들 각각을 노드에 저장 and, present 노드와 연결
    for word_index in range(len(next_words)):
      present_node.next_nodes.append(self.Node(next_words[word_index],probabilities[word_index],present_node,self.tail,num_layer))
    #present_node 다음에 또다른 계층의 노드들이 만들어졌으면, present_node가 tail 가리키면 안 되기에 tail노드로 연결된 것 끊기
    if self.tail in present_node.next_nodes:
      del present_node.next_nodes[present_node.next_nodes.index(self.tail)]

    #추천 과목 수 최대(self.num_class)로 뽑았으면(즉, present_node.num_layer==self.num_class-1), 더 이상 예측 안 할 것이기에, tail이 이 방금 생성된 마지막 단어 노드들(present_node.next_nodes)을 가리키게 하기
    if present_node.num_layer==self.num_class-1:
      for i in range(len(present_node.next_nodes)):
        self.tail.prev_node.append(present_node.next_nodes[i])
    return present_node.next_nodes#여기서 방금 예측된 단어들로부터 만들어진 노드들의 list를 return

  def predict(self,word_node,initial_state,beam_size):
    #print("word_node.word = ",word_node.word)
    word = word_node.word
    encoded_word = tf.constant([[self.vocab2idx[word]]])
    embedded_vector = self.embedding_layer(encoded_word)
    #print("lstm에 들어갈 tensor(embedded_vector) shape = \n",embedded_vector.shape)#(1,1,emb_size)여야 됨!
    hidden_states,last_hidden_state,last_cell_state = self.lstm(embedded_vector,initial_state=initial_state)
    initial_state=[last_hidden_state,last_cell_state]
    Y=self.dense(last_hidden_state)
    #print("예측된 확률 벡터 Y의 shape((1,vocab_size+1(pad, end 포함됨.)))",Y.shape)
    #print("idx2vocab 크기(위의 Y의 각 행의 크기와 동일해야 함) : ",len(self.idx2vocab))
    Y=tf.squeeze(Y)
    sorted_indices = tf.argsort(Y,axis=0,direction = "DESCENDING")
    top_k_indices = sorted_indices[:beam_size]
    top_k_indices = top_k_indices.numpy().tolist()

    next_words = [self.idx2vocab[index] for index in top_k_indices]
    probabilities_of_words = [Y[index] for index in top_k_indices]
    next_words_nodes = self.insert(next_words,probabilities_of_words,present_node = word_node,num_layer = word_node.num_layer+1)

    #이 next_words들로부터 prediction 할 것인지 확인 및 prediction(전위순회)!
    for i in range(len(next_words)):
      if next_words[i]=="<end>" or next_words[i]=="<pad>" or next_words_nodes[i].num_layer >=self.tail.num_layer:#tail.num_layer는 추천할 강의의 최대 갯수로 설정했음.
        continue
      self.predict(next_words_nodes[i],initial_state=initial_state,beam_size=beam_size)

  def search_max_prob_nodes(self,node,num_path =1):#__call__에서 node = self.tail로 뒀음!!!
    prob_list = [prev_node.probability.numpy() for prev_node in node.prev_node]#사실 node=self.tail!(즉, tail은 모든 path와 연결되어 있으니, 그걸 이용!)(각 index에는 tail.prev_node의 같은 index의 node의 probability가 저장됨.)
    #print("prob_list = ",prob_list)
    paths_probabilities = tf.constant(prob_list)
    #print("paths_probabilitie의 shape(1차원 tensor이어야 함!) = ",paths_probabilities.shape)
    sorted_indices_of_paths = tf.argsort(paths_probabilities,axis=0,direction = "ASCENDING")#노드에 저장된 probability는 축적된 확률로, -ln을 씌웠기에, 확률이 클수록, probability값은 작아지기에 오름차순으로 index를 정렬했음
    #num_path개의 후보 path를 뽑기
    top_k_indices = sorted_indices_of_paths[:num_path]
    top_k_indices = top_k_indices.numpy().tolist()
    sentences = list([])
    for index in top_k_indices:
      sentence = list([])
      word_node = node.prev_node[index]#tail에 저장된 확률이 index번째로 큰 path의 마지막 word가 저장된 node
      while True:
        if word_node != self.head:
          sentence.append(word_node.word)
          word_node = word_node.prev_node
        else:
          break
      sentence.sort()
      sentences.append(sentence)
    return sentences

#loaded_model_path = "C://Users//USER//OneDrive//바탕 화면//융합 소프트웨어//오픈소스소프트웨어프로젝트//팀프로젝트//OSSProj.ver2.0//dl//ClassRecommendModel"#windows용 주소(windows는 permission error, decoding error 등이 남.)
loaded_model_path = "/mnt/c/Users/USER/OneDrive/바탕 화면/융합 소프트웨어/오픈소스소프트웨어프로젝트/팀프로젝트/OSSProj.ver2.0/dl/ClassRecommendModel"#wsl 등 linux로 돌릴 때의 주소
# 모델 불러오기 -> 다시 새 모델 만든 데다가 embedding_matrix등의 변수 넣어 기존 훈련된 모델 완성

loaded_model = tf.keras.models.load_model(loaded_model_path,custom_objects={'Recommend_LSTM': Recommend_LSTM})#이 방식으로는 binary file을 utf-8 decoding 못해서 고쳤음.


model_config = loaded_model.get_config()
"""
# Print or use the saved variables
print(model_config)
print(model_config.keys())
"""

#기존 훈련된 모델 완성시키기(class_recommendation은 전혀 훈련 안 되어 있으니, 훈련된 가중치 넣기)
#1. 훈련 안된 모델 객체 생성 후, 객체 변수 넣기
class_recommendation =  Recommend_LSTM(vocab_size=model_config['vocab_size'],embedding_matrix=tf.constant(model_config['embedding_matrix']) , hidden_size=model_config['hidden_size'], embedding_dimension=model_config['embedding_dimension'])
idx2vocab = {int(key): value for key, value in model_config['idx2vocab'].items()}#model_config으로 딕셔너리 변수를 저장하면, 처음과 달리 key가 무조건 string이기에, 원래 숫자형이었으면, 필요에 따라 숫자형으로 바꿔주기
class_recommendation.set_vocab(vocab_size=model_config['vocab_size'],vocab2idx=model_config['vocab2idx'],idx2vocab=idx2vocab)

#2. Call the model with dummy data to ensure it is built(이걸 해서 layer들이 한 번씩 계산하도록 해야 set_weights 사용 가능!!)
dummy_input = tf.zeros(shape=(1, 20))  # Adjust the input shape based on your data
_ = class_recommendation(dummy_input)

#3. set_weights로 훈련된 가중치 넣기
dense_weights = [tf.constant(model_config['dense_weight0']),tf.constant(model_config['dense_weight1'])]
lstm_weights = [tf.constant(model_config['lstm_weight0']),tf.constant(model_config['lstm_weight1']),tf.constant(model_config['lstm_weight2'])]
class_recommendation.dense.set_weights(dense_weights)
class_recommendation.lstm.set_weights(lstm_weights)

#BeamSearch 실사용 연습
recommended_classes = class_recommendation.BeamSearch([["전자전기공학과","어드벤처디자인","신호및시스템","회로이론1","전기회로실험","디지털실험"]])#여섯개~7개정도 들었을 때, 잘 예측하는 듯
print(recommended_classes)

recommended_classes = class_recommendation.BeamSearch([["산업시스템공학과","산업시스템공학의이해","산업시스템프로그래밍1","응용통계학","경영과학1","데이터분석입문"]])#여섯개~7개정도 들었을 때, 잘 예측하는 듯
print(recommended_classes)

recommended_classes = class_recommendation.BeamSearch([["정보통신공학과","ict와소프트웨어","어드벤처디자인","정보통신프로그래밍","정보통신수학및실습","객체지향언어와실습"]])#여섯개~7개정도 들었을 때, 잘 예측하는 듯
print(recommended_classes)#산시, 전전은 잘 먹히는데, 정통은 왜? 그리고, 영어는 모두 대문자가 아닌 소문자 사용하기!