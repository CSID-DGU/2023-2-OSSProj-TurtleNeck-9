#DL코드
import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, LSTM, Layer, Activation
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
#vocab_size = len(self.vocab2idx) + 1
excel_address='/content/drive/MyDrive/융소_ossp_수강추천시스템DL/OSSProj_DL_sign-up-course/sample_classes.xlsx'
class Recommend_LSTM(Model):
  def __init__(self,address,hidden_size=8,embedding_dimension=16):#hidden_size는 LSTM의 출력값 hidden_state의 차원 의미
    super().__init__()
    self.embedding_dimension=embedding_dimension
    self.hidden_size=hidden_size
    self.tokenizer = Tokenizer()
    self.vocab_size,self.vocab2idx,self.idx2vocab,self.encoded_data_list=self.data_preprocessing_encoding(excel_address=address,tokenizer = Tokenizer())
    self.embedding_layer = Embedding(input_dim=self.vocab_size, output_dim=embedding_dimension, input_shape=(None,))
    self.embedding_layer, self.encoded_data_list_answer_padded, self.encoded_data_list_input_padded=self.data_preprocessing_SGNS(vocab_size=self.vocab_size,encoded_data_list=self.encoded_data_list,embedding_dimension=self.embedding_dimension,embedding_layer =self.embedding_layer)
    #self.embedding_layer, self.vocab2idx, self.idx2vocab, self.encoded_data_list_answer_padded, self.encoded_data_list_input_padded = data_preprocessing(excel_address=address,embedding_dimension=self.embedding_dimension,tokenizer=self.tokenizer)
    self.lstm=LSTM(units=hidden_size, return_sequences=True, return_state=True)
    vocab_size = len(self.idx2vocab)
    self.dense = Dense(units=vocab_size,activation="softmax")#Dense laye는 입력값의 차원과 출력값의 차원 수 동일(즉, 3차원 Tensor가 입력되면, 3차원 Tensor가 출력)한데, softmax를 썼으니,  출력값은 (sample수,문장길이,vocab_size)로써, 훈련시 정답 label과 최대한 비슷하게 되므로,

  """
  def build(self, input_shape):#build는 fit, evaluate, predict 메서드 사용시에 호출되지만, call 메서드 실행시에는 작동되지 않음!(즉, 훈련된 가중치 유지됨!)
    vocab_size = len(self.idx2vocab)
    self.embedding_layer.build((None, self.embedding_dimension))#Embedding 레이어는 (sample 수, 문장 길이)와 같은 2D 입력을 받지만. None은 어떤 길이의 문장도 처리할 수 있음을 나타내기에, None을 쓴 것!(사실, padding 해놓은 데이터 셋이 fit할 때, input으로 들어가기에, 문장 길이 고정되어 있긴 함!)
    self.lstm.build((None, None, self.embedding_dimension))  # Adjust input shape accordingly
    self.dense.build((None, None, self.hidden_size))
  """

  def __call__(self,encoded_classes_list,training=False):
    X=self.embedding_layer(encoded_classes_list)
    X=self.lstm(X)[0]#return_sequences=True, return_state=True로 하였으니, hidden_states(lstm layer의 출력값)의 shape = (sample수, 문장길이, hidden_size) -> hidden size 크기의 행벡터들 각각은 단어에 해당
    X=self.dense(X)#이렇게 dense layer을 통해 나온 각 단어에 대한 각각의 확률벡터에서 가장 큰 index가 정답 label(self.encoded_data_list_answer_padded)가 최대한 되도록 훈련시키는 것!
    return X

  def data_preprocessing_encoding(self,excel_address,tokenizer = Tokenizer()):#excel_address는 전처리할 훈련데이터 저장 주소임.
  #excel 파일 받기
  #tokenizer로 토큰화 하기 위해선, 문장 string이 하나의 원소인 list or 이미 토큰화된 단어들로 이뤄진 문장이 list로서 하나의 원소인 list가 입력값이 되어야 하니 -> dataframe을 2차원 list로(dataframe은 행렬이니, 이미 토큰화 된 것이나 마찬가지)
  #각 행이 문장이니 각 list의 원소(=하나의 문장(=list))의 빈 원소(None)들은 제거
  #tokenizer로 정수 인코딩, 어휘 사전 만들기(padding token(0)에 대한 emb. vector도 embedding table에 들어있게 하기 위해 vocab_size=어휘사전 크기+1 하기 )
  #SGNS로 embedding table만들기
  #padding
  #return은 embedding table, 어휘사전(vocab2idx, idx2vocab), 정수 encoding된 data_list(for 정답 label = 첫번째 열 제거), embedding된 data_list(for 입력 = 마지막 열 제거 - padding 전에 제거해야 됨!) 아님  정수 encoding된 data_list(for 입력 = 마지막 열 제거 - padding 전에!)

  #1. excel 파일(훈련데이터) 받기
    df = pd.read_excel(excel_address)
    print("raw data df = \n",df)

    #2.dataframe df -> list로
    raw_data_list = df.values.tolist()#그냥 tolist만으로 데이터 프레임은 2차원 list가 된다
    print("raw_data_list = \n",raw_data_list)

    #3.list의 각 원소(list로 된 문장)에서 Nan인 부분만 제거(list 전체가 아니라!)
    NanX_data_list = [[value for value in row if pd.notna(value)] for row in raw_data_list]#리스트 컴프리헨션 : 각 문장(raw)들은 nan값이 제거된 문장([value for value in row if pd.notna(value)])들이 되어 NanX_data_list를 이룬다.
    print("Nan_elimiated_list = \n",NanX_data_list)
      #end 패드 각 문장마다 마지막에 넣기
    NanX_data_list_endpad=[]
    for sentence in NanX_data_list:
      sentence.append("<end>")
      NanX_data_list_endpad.append(sentence)
    NanX_data_list = NanX_data_list_endpad
    print("NanX_data_list[0] = \n",NanX_data_list[0])

    #4. tokenizer로 정수 인코딩, 어휘 사전 만들기
    #tokenizer = Tokenizer()
    tokenizer.fit_on_texts(NanX_data_list)#토큰화까지 완료된 sentence 집합(각 sentence들은 list들이 되어 있고, 이 list들이 하나의 list로 묶여있는 데이터)을 입력한 것으로, 여기선 multi_label이 이에 해당 | but 각 sentence들이 String(토큰화 x)인 상태인 1차원 list를 입력하면, 토큰화까지 자동으로 해줌!
      #즉, tokenizer.fit_on_texts(sentences)는 각 원소들이 string으로 된 문장들의 list를 받아 토큰화+이로부터 단어집합을 만들거나 이미
    #4-1.어휘사전 만들기
    vocab2idx = tokenizer.word_index#단어 집합(어휘사전)

    #4-2. 정수 인코딩
    encoded_data_list=tokenizer.texts_to_sequences(NanX_data_list)#토큰화된 sample 문장들의 각 토큰을 정수로 -> 나중에 패딩 후, 각 정수는 embedding vector들로 표현되어 input 데이터가 될 것!
      #tokennizer로부터 encoding된 multi_label 구하면, 이는 list!

    vocab_size = len(vocab2idx) + 1  # 단어 집합(vocabulary)의 크기를 어휘 사전(word2idx)의 길이에 1을 더한 이유는 일반적으로 자연어 처리 모델에서 사용되는 토큰 중 하나를 예약(reserved)하기 위해서입니다. 이 토큰은 텍스트에서 특정 단어가 아닌 "알 수 없는 단어" 또는 "패딩"을 나타내는데 사용됩니다.(나중에 embedding layer에서 vocab_size가 input_dim에 들어가 input_dim이 embedding Table이 행이 되기 때문에, 각 행이 각 word에 대응되려면, padding나타내는 단어는 0에 대응되게 하기 위해선, 실제 단어수+1(len(id2vocab))을 해야함!)
    print('단어 집합의 크기 :', vocab_size)
    idx2vocab = {value : key for key, value in vocab2idx.items()}#어휘사전 vocab은 key가 단어 즉, string이라서, 이후, 네거티브 샘플링이 잘 되었는지(데이터 셋이 올바르게 중심, 주변 단어로 짝지어져 있는지) 단어로 확인하려면, indexing으로 확인해야 하지만, key가 string, value가 index인 상태라 불가능하다. -> key-value 관계를 반대로 할 필요!
    idx2vocab[0] = "<pad>"#나중에 예측 문장 확인할 때 0을 바꿀 때 사용 (실제로 SGNS의 embedding matrix에서 0행은 제로패딩시의 token의 embedding vector여야 하기에!!!)
    print("idx2vocab = ",idx2vocab)
    return vocab_size,vocab2idx,idx2vocab,encoded_data_list

  def data_preprocessing_SGNS(self,vocab_size,encoded_data_list,embedding_dimension=16,embedding_layer = Embedding(input_dim=105, output_dim=16, input_shape=(None,))):#105는 vocab_size, 16은 embedding_dim이지만, 사실 모델 클래스에서 Embedding layer 직접 넣을 것이기에 상관 x!
    #5. SGNS
      #5-1 : SGNS 모델 구성
    input_center = Input(shape=(1,), dtype=tf.int32)
    input_context = Input(shape=(1,), dtype=tf.int32)
    #embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dimension, input_shape=(None,))#주의 : embeddingLayer 객체 생성시, input_dim(즉, emb_table의 열 개수)는 내가 처음 집어넣을 전체 데이터 셋의 모든 단어 종류 수보다 1많게 해야 한다1(index=0인 행은 padding단어니까!) | 즉, vocab_size = len(idx2vocab)이 됨! - 밑에서 emb_layer에 들어갈 dataset은 encoded_data_list로 패딩 전 거라서!
    center_embedding = embedding_layer(input_center)#중심단어(input_center)의 정수 인코딩(or one-hot)에 해당하는 embedding table의 행 객체 의미(print해보면, 느낌 옴.)
    context_embedding = embedding_layer(input_context)#주변 단어 ...
    dot_product = Dot(axes=2)([center_embedding, context_embedding])#두 emb vector의 내적
    output = Dense(1, activation='sigmoid')(dot_product)#이 것에 sigmoid만 씌운 것
    model = tf.keras.Model(inputs=[input_center, input_context], outputs=output)

      #5-2 : SGNS 시작(skip-gram 위한 데이터 셋 만들기 -> model 학습)
        # 손실 함수 정의 및 모델 컴파일
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        #SGNS 모델 학습
    for epoch in range(1, 2):
        #네거티브 샘플링
      skip_grams = [skipgrams(sample, vocabulary_size=vocab_size, window_size=2) for sample in encoded_data_list]#skipgrams 함수는 Skip-gram 모델을 학습하기 위해 필요한 학습 데이터를 생성하는 역할 -> 즉, SGNS 데이터셋을 만드는 과정 참고해보면,
            #즉, epoch마다 다시 랜덤으로 틀린 쌍을 생성하여 맞는 쌍과 함께 조합하여 새로운 학습데이터를 만드는 부분(위의 self.skip_grams는) -> model.fit을 dataset.shuffle을 epoch마다 하는 것과 마찬가지
            #window_size=2란, center_word로부터 양 옆 한 칸씨과만 비교
      loss = 0
      for _, elem in enumerate(skip_grams):#skip_gram 구조를 보면, 알 수 있듯, elem은 하나의 토큰화되어 정수인코딩된 문장의 각 중심,주변 단어 쌍들을 list로 모아 하나의 list로/ 그리고, 각 쌍들에 대한 정답 label을 모다 list로 만들어 이 두 list를 쌍으로 갖는 튜플이다.
        first_elem = np.array(list(zip(*elem[0]))[0], dtype='int32')
  #     print("first_elem : \n",first_elem)
        second_elem = np.array(list(zip(*elem[0]))[1], dtype='int32')
  #     print("second_elem : \n",second_elem)
        labels = np.array(elem[1], dtype='int32')
  #     print("labels : \n",labels)
        X = [first_elem.reshape(-1,1), second_elem.reshape(-1,1)]#훈련 데이터셋을 교재(wikidox)처럼 2열짜리(하나의 열은 center, 나머지 하나는 context(주변) 단어 후보)로 맞춘 것
        Y = labels.reshape(-1,1)#출력값 형태에 맞게(1열 벡터) 정답 라벨 구성
        loss += model.train_on_batch(X,Y)[0]
  #      accuracy=  model.train_on_batch(X,Y)[1]
  #    print('Epoch :',epoch, 'Loss :',loss, 'accuracy : ',accuracy)
    print('Epoch :',epoch, 'Loss :',loss)
      # 단어 임베딩 추출
    word_embedding_table = embedding_layer.get_weights()[0]#이 행렬이 바로 embedding table로 각 행이 단어들의 embedding vector
  #    word_embeddings_bias = embedding_layer.get_weights()[1] -> index out of range 오류가 나는 것으로 보아, Embedding layer는 bias는 없고, 가중치가 embedding table만 있음을 알 수 있다.
    print("embedding tabel shape : ",word_embedding_table.shape)
    print("type(word_embeddings_table) : ",type(word_embedding_table))

  #보통 학생들이 듣는 과목수를 모두 세어 maxlen을 결정(너무 많은 padding이 되지 않게)
    print('수강한 최대 과목수 :',max(len(sample_list) for sample_list in encoded_data_list))
    print('수강한 평균 과목수 :',sum(map(len, encoded_data_list))/len(encoded_data_list))
    plt.hist([len(sample_list) for sample_list in encoded_data_list], bins=50)
    plt.xlabel('들은 과목수(=문장 길이)')
    plt.ylabel('샘플 수(=학생 수)')
    plt.show()

    #max_len=input("패딩길이를 결정하세요 : ")#그래프를 보고 너무 적은 수의 문장들이 매우 긴 경우, maxlen을 이보다 작은 수로 설정해 그들은 바로 밑의 코드를 통해 제거할 것
    max_len=30;#데이터 셋 너무 커서 input이 안 먹혀서 그래프 보고 설정한 것(30이상은 거의 없어서 뺄 것)
    lower_lim=25#25미만의 데이터 셋은 거의 없으니 제거할 것

    #maxlen을 결정했으면, maxlen보다 긴 sample들은 제거*(encoded_data_list에서) -> 제거된 상태의 encoded_data_list에서 정답라벨, 훈련 데이터셋 만들고(6.), 패딩(7.)
    encoded_data_list = [sample_list for sample_list in encoded_data_list if len(sample_list)<=max_len and (len(sample_list))>=lower_lim]
    print("패딩 전, 일정 길이의 sample만 뽑은 정수 인코딩된 data list(encoded_data_list) : ")
    print(encoded_data_list[0:3])

    #제대로 샘플들 선택했는지(lower_lim 이상, max_len 이하로)
    print('수강한 최대 과목수 :',max(len(sample_list) for sample_list in encoded_data_list))
    print('수강한 평균 과목수 :',sum(map(len, encoded_data_list))/len(encoded_data_list))
    plt.hist([len(sample_list) for sample_list in encoded_data_list], bins=50)
    plt.xlabel('들은 과목수(=문장 길이)')
    plt.ylabel('샘플 수(=학생 수)')
    plt.show()
    """#아래 방식으로 바꿨음!!!
    #패딩 전에 return값의 마지막 2개부터 만들고, 이 둘을 각각 패딩!(6,7 순서 바꿔야될 수도 있음! - 모델 다 만들고 해보기!)
      #6. 정답 label(정수 인코딩된 label(encoded_data_list)에서 첫번째 단어들만 삭제), 훈련 데이터 만들기(정수 인코딩된 label(encoded_data_list)에서 마지막 단어들만 삭제)
    encoded_data_list_answer = [sentence[1:] for sentence in encoded_data_list]#정답 label-첫 단어만 빠졌는지 확인
    encoded_data_list_input = [sentence[:len(sentence)-1] for sentence in encoded_data_list]#input data - 마지막 단어(end패드)

      #정답 라벨이 훈련 데이터에 비해 단어(정수 인코딩된)들이 한칸씩 먼저 나오는지 확인(for 실제 운용시, 입력된 기수강과목으로부터 마지막으로 들은 과목으로부터 이후에 들을 과목을 예측하기 위해서 = 즉, 다음에 들을(나올) 단어를 예측하는 겄!)
    print("정답 label(첫 단어들만 빠졌는지 확인) = \n",encoded_data_list_answer)
    print("훈련 데이터(마지막 단어들만 빠졌는지 확인) = \n",encoded_data_list_input)

      #7. padding
    print('문장의 최대 길이(original data) :',max(len(sentence) for sentence in encoded_data_list))#첫 단어 or 마지막 단어는 제거되니 padding에 사용할 최대 문장 길이는 -1하기!(pad_sequences부분 참고)
    #  max_len = max(len(sentence) for sentence in encoded_data_list)
    encoded_data_list_answer_padded = pad_sequences(encoded_data_list_answer, maxlen=max_len-1,padding='post')
    encoded_data_list_input_padded = pad_sequences(encoded_data_list_input, maxlen=max_len-1,padding='post')
    print("패딩 정답 label = \n", encoded_data_list_answer_padded)
    print("패딩 훈련 label = \n", encoded_data_list_input_padded)
    """
    #6. padding
    encoded_data_list_padded = pad_sequences(encoded_data_list, maxlen=max_len,padding='post')
    print("패딩된 정수 인코딩 list = \n",encoded_data_list_padded)

    #7. 정답 label(정수 인코딩된 label(encoded_data_list)에서 첫번째 단어들만 삭제), 훈련 데이터 만들기(정수 인코딩된 label(encoded_data_list)에서 마지막 단어들만 삭제)
    encoded_data_list_answer_padded = [sentence[1:] for sentence in encoded_data_list_padded]#정답 label-첫 단어만 빠졌는지 확인
    encoded_data_list_input_padded = [sentence[:len(sentence)-1] for sentence in encoded_data_list_padded]#input data - 마지막 단어(end패드)
    print("패딩 정답 label = \n", encoded_data_list_answer_padded)
    print("패딩 훈련 label = \n", encoded_data_list_input_padded)
    return embedding_layer, encoded_data_list_answer_padded, encoded_data_list_input_padded



  class Node():
    def __init__(self, word, probability, prev_node, next_nodes, num_layer):
      self.word = word
      if num_layer==0 or type(prev_node) == list or type(prev_node) == type(None):#self.head는 num_layer=0, prev_node=None임 / self.tail만 self.tail.prev_node를 list로 하여 노드 객체 리스트로 여러 노드를 저장하기 때문 -> 이 if문은 현재 생성되는 노드가 head or tail임을 검사한다.
        print("현재 생성되는 노드는 head or tail이다.")
        self.probability = -tf.math.log(probability)
        print("{}의 probability : {}, -tf.math.log(probability) : {},누적확률 : {}".format(self.word,probability,-tf.math.log(probability),self.probability))

      else:#실제 과목을 저장하고 있는 노드
        self.probability=prev_node.probability-tf.math.log(probability)
      self.prev_node = prev_node
      self.next_nodes = next_nodes#이 노드 객체의 word로부터 딥러닝 모델을 거처 예상된 k개의 후보 단어들을 저장할 각각의 노드들로, list에 노드들이 각각 들어갈 것임
      self.num_layer = num_layer#이 노드가 몇 번째 layer에 있는지 의미(int임)

  def BeamSearch(self,taken_classes,num_class=5,beam_size=3):
    self.head = self.Node(word="head",probability=1.0,prev_node=None,next_nodes=None,num_layer=0);self.tail=self.Node("tail",1.0,prev_node=list([]),next_nodes=None,num_layer=num_class)
    self.head.next_nodes=self.tail
    #첫번째 예측 단어들의 확률 계산
    self.num_class=num_class
    encoded_data = self.tokenizer.texts_to_sequences(taken_classes)
    encoded_data = tf.constant(encoded_data)
    print("정수 인코딩된 기수강 과목들(encoded_data)의 shape = \n",encoded_data.shape)#(2차원 텐서(즉 행렬)여야 한다! -> 그래야 embedding_layer지나면, 3차원이 되어 lstm을 문제없이 지나니까)
    X = self.embedding_layer(encoded_data)
    print("lstm 입력될 텐서 shape(X) = ",X.shape)
    hidden_states, last_hidden_state, last_cell_state = self.lstm(X)
    initial_state = [last_hidden_state, last_cell_state]
    probabilities = self.dense(last_hidden_state)
    print("last_hidden_state의 shape = (1,vocab_size+1)이어야됨. \n",last_hidden_state.shape)
    probabilities = tf.squeeze(probabilities)
    #가장 확률 큰 beamsize개의 예측 단어 찾아 각각 노드에 저장 and head와 연결
    sorted_indices = tf.argsort(probabilities,axis=0,direction="DESCENDING")
    top_k_indices = sorted_indices[:beam_size]
    top_k_indices = top_k_indices.numpy().tolist()
    words = [self.idx2vocab[index] for index in top_k_indices]#첫번째 예상 단어 후보 리스트
    print("첫번째 예상 단어 후보 리스트 : ",words)
    probabilities_of_words = [probabilities[index] for index in top_k_indices]
    print("첫번째 예상 단어 후보 각각에 대응되는 확률 리스트: ",probabilities_of_words)
    #노드에 저장 및 head와 연결
    words_nodes = self.insert(words,probabilities_of_words,self.head,num_layer=1)

    print("word_nodes = ",words_nodes)
    #각 첫번째 예측 단어 후보들(words_nodes들의 원소(노드)들)로부터 똑같이 후보 예측 and 현재 노드(words_nodes의 원소)에 연결
    for word_node in words_nodes:
      print("word_node = ",word_node)
      self.predict(word_node,initial_state,beam_size)

    #후보 path(추천 과목 모음)들 찾기(num_path만큼)
    sentences = self.search_max_prob_nodes(self.tail,num_path=10)

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
#    print("present_node.next_nodes = ",present_node.next_nodes)
    return present_node.next_nodes#여기서 방금 예측된 단어들로부터 만들어진 노드들의 list를 return

  def predict(self,word_node,initial_state,beam_size):
#    print("word_node = ",word_node)
#    print("에러부분")
    print("word_node.word = ",word_node.word)
    word = word_node.word
    encoded_word = tf.constant([[self.vocab2idx[word]]])
    embedded_vector = self.embedding_layer(encoded_word)
    print("lstm에 들어갈 tensor(embedded_vector) shape = \n",embedded_vector.shape)#(1,1,emb_size)여야 됨!
    hidden_states,last_hidden_state,last_cell_state = self.lstm(embedded_vector,initial_state=initial_state)
    initial_state=[last_hidden_state,last_cell_state]
    Y=self.dense(last_hidden_state)
    print("예측된 확률 벡터 Y의 shape((1,vocab_size+1(pad, end 포함됨.)))",Y.shape)
    print("idx2vocab 크기(위의 Y의 각 행의 크기와 동일해야 함) : ",len(self.idx2vocab))
    Y=tf.squeeze(Y)
    sorted_indices = tf.argsort(Y,axis=0,direction = "DESCENDING")
    top_k_indices = sorted_indices[:beam_size]
    top_k_indices = top_k_indices.numpy().tolist()

    next_words = [self.idx2vocab[index] for index in top_k_indices]
    probabilities_of_words = [Y[index] for index in top_k_indices]
    next_words_nodes = self.insert(next_words,probabilities_of_words,present_node = word_node,num_layer = word_node.num_layer+1)

#    print("next_words 원소 수 : ",len(next_words))
#    print("next_words_nodes 원소 수(next_words 원소 각각이 노드에 저장되니 개수가 next_words와 동일해야 함!) : ",len(next_words_nodes))

    #이 next_words들로부터 prediction 할 것인지 확인 및 prediction(전위순회)!
    for i in range(len(next_words)):
      if next_words[i]=="<end>" or next_words[i]=="<pad>" or next_words_nodes[i].num_layer >=self.tail.num_layer:#tail.num_layer는 추천할 강의의 최대 갯수로 설정했음.
        continue
      self.predict(next_words_nodes[i],initial_state=initial_state,beam_size=beam_size)

  def search_max_prob_nodes(self,node,num_path =10):#__call__에서 node = self.tail로 뒀음!!!
    prob_list = [prev_node.probability.numpy() for prev_node in node.prev_node]#사실 node=self.tail!(즉, tail은 모든 path와 연결되어 있으니, 그걸 이용!)(각 index에는 tail.prev_node의 같은 index의 node의 probability가 저장됨.)
    print("prob_list = ",prob_list)
    paths_probabilities = tf.constant(prob_list)
    print("paths_probabilitie의 shape(1차원 tensor이어야 함!) = ",paths_probabilities.shape)
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
