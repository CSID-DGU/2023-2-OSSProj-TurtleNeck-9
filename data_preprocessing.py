#훈련 데이터 전처리
# 추가할 것 : 각 학기 별로 특정(상대적인) 순서로 정렬하는 코드 짜기(1. or 2.에서!!!), 진로 열 빼기(1.에서)
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, Layer, Activation
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.preprocessing.sequence import pad_sequences#문장 패딩해주는 애
import numpy as np
import pandas as pd
def data_preprocessing(embedding_dimension=16):
  #excel 파일 받기
  #tokenizer로 토큰화 하기 위해선, 문장 string이 하나의 원소인 list or 이미 토큰화된 단어들로 이뤄진 문장이 list로서 하나의 원소인 list가 입력값이 되어야 하니 -> dataframe을 2차원 list로(dataframe은 행렬이니, 이미 토큰화 된 것이나 마찬가지)
  #각 행이 문장이니 각 list의 원소(=하나의 문장(=list))의 빈 원소(None)들은 제거
  #tokenizer로 정수 인코딩, 어휘 사전 만들기(padding token(0)에 대한 emb. vector도 embedding table에 들어있게 하기 위해 vocab_size=어휘사전 크기+1 하기 )
  #SGNS로 embedding table만들기
  #padding
  #return은 embedding table, 어휘사전(vocab2idx, idx2vocab), 정수 encoding된 data_list(for 정답 label = 첫번째 열 제거), embedding된 data_list(for 입력 = 마지막 열 제거 - padding 전에 제거해야 됨!) 아님  정수 encoding된 data_list(for 입력 = 마지막 열 제거 - padding 전에!)

  #1. excel 파일(훈련데이터) 받기
  df = pd.read_excel('C:\Users\USER\OneDrive\바탕 화면\융합 소프트웨어\오픈소스소프트웨어프로젝트\수강신청데이터.xlsx')
  print("raw data df = \n",df)
  #진로 열 빼기!
  #원래는 여기서 학기 별로 특정 순서에 맞게 정렬하면, 더 정확한 DB 만들 수 있음

  #2.dataframe df -> list로
  raw_data_list = df.values.tolist()#그냥 tolist만으로 데이터 프레임은 2차원 list가 된다

  print("raw_data_list = \n",raw_data_list)

  #3.list의 각 원소(list로 된 문장)에서 Nan인 부분만 제거(list 전체가 아니라!)
  NanX_data_list = [[value for value in row if pd.notna(value)] for row in raw_data_list]#리스트 컴프리헨션 : 각 문장(raw)들은 nan값이 제거된 문장([value for value in row if pd.notna(value)])들이 되어 NanX_data_list를 이룬다.
  print("Nan_elimiated_list = \n",NanX_data_list)
    #end 패드 각 문장마다 마지막에 넣기
  NanX_data_list = [sentence.append("end") for sentence in NanX_data_list]

  #4. tokenizer로 정수 인코딩, 어휘 사전 만들기
  tokenizer = Tokenizer()
  tokenizer.fit_on_texts(NanX_data_list)#토큰화까지 완료된 sentence 집합(각 sentence들은 list들이 되어 있고, 이 list들이 하나
     #즉, tokenizer.fit_on_texts(sentences)는 각 원소들이 string으로 된 문장들의 list를 받아 토큰화+이로부터 단어집합을 만들거나 이미
  #4-1.어휘사전 만들기
  vocab2idx = tokenizer.word_index#단어 집합(어휘사전)

  #4-2. 정수 인코딩
  encoded_data_list=tokenizer.texts_to_sequences(NanX_data_list)#토큰화된 sample 문장들의 각 토큰을 정수로 -> 나중에 패딩 후, 각 정수는 embedding vector들로 표현되어 input 데이터가 될 것!
    #tokennizer로부터 encoding된 multi_label 구하면, 이는 list!

  vocab_size = len(vocab2idx) + 1  # 단어 집합(vocabulary)의 크기를 어휘 사전(word2idx)의 길이에 1을 더한 이유는 일반적으로 자연어 처리 모델에서 사용되는 토큰 중 하나를 예약(reserved)하기 위해서입니다. 이 토큰은 텍스트에서 특정 단어가 아닌 "알 수 없는 단어" 또는 "패딩"을 나타내는데 사용됩니다.
  print('단어 집합의 크기 :', vocab_size)
  idx2vocab = {value : key for key, value in vocab2idx.items()}#어휘사전 vocab은 key가 단어 즉, string이라서, 이후, 네거티브 샘플링이 잘 되었는지(데이터 셋이 올바르게 중심, 주변 단어로 짝지어져 있는지) 단어로 확인하려면, indexing으로 확인해야 하지만, key가 string, value가 index인 상태라 불가능하다. -> key-value 관계를 반대로 할 필요!
  idx2vocab[0] = ""#나중에 예측 문장 확인할 때 0을 바꿀 때 사용 (실제로 SGNS의 embedding matrix에서 0행은 제로패딩시의 token의 embedding vector여야 하기에!!!)
  print("idx2vocab = ",idx2vocab)

  #5. SGNS
    #5-1 : SGNS 모델 구성
  input_center = Input(shape=(1,), dtype=tf.int32)
  input_context = Input(shape=(1,), dtype=tf.int32)
  embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dimension)
  center_embedding = embedding_layer(input_center)#중심단어(input_center)의 정수 인코딩(or one-hot)에 해당하는 embedding table의 행 객체 의미(print해보면, 느낌 옴.)
  context_embedding = embedding_layer(input_context)#주변 단어 ...
  dot_product = Dot(axes=2)([center_embedding, context_embedding])#두 emb vector의 내적
  output = Dense(1, activation='sigmoid')(dot_product)#이 것에 sigmoid만 씌운 것
  model = tf.keras.Model(inputs=[input_center, input_context], outputs=output)

    #5-2 : SGNS 시작(skip-gram 위한 데이터 셋 만들기 -> model 학습)
      # 손실 함수 정의 및 모델 컴파일
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
      #SGNS 모델 학습
  for epoch in range(1, 6):
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
      loss += model.train_on_batch(X,Y)
#      accuracy=  model.train_on_batch(X,Y)[1]
#    print('Epoch :',epoch, 'Loss :',loss, 'accuracy : ',accuracy)
  print('Epoch :',epoch, 'Loss :',loss)
    # 단어 임베딩 추출
  word_embedding_table = embedding_layer.get_weights()[0]#이 행렬이 바로 embedding table로 각 행이 단어들의 embedding vector
#    word_embeddings_bias = embedding_layer.get_weights()[1] -> index out of range 오류가 나는 것으로 보아, Embedding layer는 bias는 없고, 가중치가 embedding table만 있음을 알 수 있다.
  print("embedding tabel shape : ",word_embedding_table.shape)
  print("type(word_embeddings_table) : ",type(word_embedding_table))

#패딩 전에 return값의 마지막 2개부터 만들고, 이 둘을 각각 패딩!
  #6. 정답 label(정수 인코딩된 label(encoded_data_list)에서 첫번째 단어들만 삭제), 훈련 데이터 만들기(정수 인코딩된 label(encoded_data_list)에서 마지막 단어들만 삭제)
  encoded_data_list_answer = [sentence[1:] for sentence in encoded_data_list]#정답 label-첫 단어만 빠졌는지 확인
  encoded_data_list_input = [sentence[:len(sentence)-1] for sentence in encoded_data_list]#input data - 마지막 단어(end패드 말고)(sentence[len(sentence)-1])만 빠졌는지 확인
  encoded_data_list_input = []


  print("정답 label(첫 단어들만 빠졌는지 확인) = \n",encoded_data_list_answer)
  print("훈련 데이터(마지막 단어들만 빠졌는지 확인) = \n",encoded_data_list_input)

  #7. padding
  print('문장의 최대 길이(original data) :',max(len(sentence) for sentence in encoded_data_list))#첫 단어 or 마지막 단어는 제거되니 padding에 사용할 최대 문장 길이는 -1하기!
  max_len = max(len(sentence) for sentence in encoded_data_list)-1
  encoded_data_list_answer_padded = pad_sequences(encoded_data_list_answer, maxlen=max_len,padding='post')
  encoded_data_list_input_padded = pad_sequences(encoded_data_list_input, maxlen=max_len,padding='post')
  print("패딩 정답 label = \n", encoded_data_list_answer_padded)
  print("패딩 훈련 label = \n", encoded_data_list_input_padded)
#훈련 데이터 패딩은 Neural net에서 할 것
  return word_embedding_table, vocab2idx, idx2vocab, encoded_data_list_answer_padded, encoded_data_list_input_padded