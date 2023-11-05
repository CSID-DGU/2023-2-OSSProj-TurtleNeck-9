#실제 데이터 전처리 코드(이 함수를 DL 클래스에서 쓰기 위해, tokenizer을 input값으로 추가한 것 밖에 없다.)
#훈련 데이터 전처리
# 추가할 것 : 각 학기 별로 특정(상대적인) 순서로 정렬하는 코드 짜기(1. or 2.에서!!!), 진로 열 빼기(1.에서)
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, Layer, Activation
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.preprocessing.sequence import pad_sequences#문장 패딩해주는 애
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def data_preprocessing(excel_address,embedding_dimension=16,tokenizer = Tokenizer()):#excel_address는 전처리할 훈련데이터 저장 주소임.
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

  #5. SGNS
    #5-1 : SGNS 모델 구성
  input_center = Input(shape=(1,), dtype=tf.int32)
  input_context = Input(shape=(1,), dtype=tf.int32)
  embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dimension)#주의 : embeddingLayer 객체 생성시, input_dim(즉, emb_table의 열 개수)는 내가 처음 집어넣을 전체 데이터 셋의 모든 단어 종류 수보다 1많게 해야 한다1(index=0인 행은 padding단어니까!) | 즉, vocab_size = len(idx2vocab)이 됨! - 밑에서 emb_layer에 들어갈 dataset은 encoded_data_list로 패딩 전 거라서!
  center_embedding = embedding_layer(input_center)#중심단어(input_center)의 정수 인코딩(or one-hot)에 해당하는 embedding table의 행 객체 의미(print해보면, 느낌 옴.)
  context_embedding = embedding_layer(input_context)#주변 단어 ...
  dot_product = Dot(axes=2)([center_embedding, context_embedding])#두 emb vector의 내적
  output = Dense(1, activation='sigmoid')(dot_product)#이 것에 sigmoid만 씌운 것
  model = tf.keras.Model(inputs=[input_center, input_context], outputs=output)

    #5-2 : SGNS 시작(skip-gram 위한 데이터 셋 만들기 -> model 학습)
      # 손실 함수 정의 및 모델 컴파일
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
      #SGNS 모델 학습
  for epoch in range(1, 10):
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
  print(encoded_data_list[0:3])

  #제대로 샘플들 선택했는지(lower_lim 이상, max_len 이하로)
  print('수강한 최대 과목수 :',max(len(sample_list) for sample_list in encoded_data_list))
  print('수강한 평균 과목수 :',sum(map(len, encoded_data_list))/len(encoded_data_list))
  plt.hist([len(sample_list) for sample_list in encoded_data_list], bins=50)
  plt.xlabel('들은 과목수(=문장 길이)')
  plt.ylabel('샘플 수(=학생 수)')
  plt.show()

  #패딩 전에 return값의 마지막 2개부터 만들고, 이 둘을 각각 패딩!
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
#훈련 데이터 패딩은 Neural net에서 할 것
  return embedding_layer, vocab2idx, idx2vocab, encoded_data_list_answer_padded, encoded_data_list_input_padded

#data_preprocessing('/content/drive/MyDrive/융소_ossp_수강추천시스템DL/OSSProj_DL_sign-up-course/sample_classes.xlsx')
