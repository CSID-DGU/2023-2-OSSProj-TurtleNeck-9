import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.layers import Input, Embedding, Dot, Dense, Layer, Activation
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def data_preprocessing(excel_address,embedding_dimension=16,tokenizer = Tokenizer()):
  df = pd.read_excel(excel_address)
  print("raw data df = \n",df)

  raw_data_list = df.values.tolist()

  print("raw_data_list = \n",raw_data_list)

  NanX_data_list = [[value for value in row if pd.notna(value)] for row in raw_data_list]
  print("Nan_elimiated_list = \n",NanX_data_list)
  NanX_data_list_endpad=[]
  for sentence in NanX_data_list:
    sentence.append("<end>")
    NanX_data_list_endpad.append(sentence)
  NanX_data_list = NanX_data_list_endpad
  print("NanX_data_list[0] = \n",NanX_data_list[0])


  tokenizer.fit_on_texts(NanX_data_list)
  vocab2idx = tokenizer.word_index

  encoded_data_list=tokenizer.texts_to_sequences(NanX_data_list)

  vocab_size = len(vocab2idx) + 1 
  print('단어 집합의 크기 :', vocab_size)
  idx2vocab = {value : key for key, value in vocab2idx.items()}
  idx2vocab[0] = "<pad>"
  print("idx2vocab = ",idx2vocab)

  input_center = Input(shape=(1,), dtype=tf.int32)
  input_context = Input(shape=(1,), dtype=tf.int32)
  embedding_layer = Embedding(input_dim=vocab_size, output_dim=embedding_dimension)
  center_embedding = embedding_layer(input_center)
  context_embedding = embedding_layer(input_context)
  dot_product = Dot(axes=2)([center_embedding, context_embedding])
  output = Dense(1, activation='sigmoid')(dot_product)
  model = tf.keras.Model(inputs=[input_center, input_context], outputs=output)

  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
     
  for epoch in range(1, 10):
    skip_grams = [skipgrams(sample, vocabulary_size=vocab_size, window_size=2) for sample in encoded_data_list]
    loss = 0
    for _, elem in enumerate(skip_grams):
      first_elem = np.array(list(zip(*elem[0]))[0], dtype='int32')
      second_elem = np.array(list(zip(*elem[0]))[1], dtype='int32')
      labels = np.array(elem[1], dtype='int32')
      X = [first_elem.reshape(-1,1), second_elem.reshape(-1,1)]
      Y = labels.reshape(-1,1)
      loss += model.train_on_batch(X,Y)[0]
  print('Epoch :',epoch, 'Loss :',loss)
  word_embedding_table = embedding_layer.get_weights()[0]
  print('수강한 최대 과목수 :',max(len(sample_list) for sample_list in encoded_data_list))
  print('수강한 평균 과목수 :',sum(map(len, encoded_data_list))/len(encoded_data_list))
  plt.hist([len(sample_list) for sample_list in encoded_data_list], bins=50)
  plt.xlabel('들은 과목수(=문장 길이)')
  plt.ylabel('샘플 수(=학생 수)')
  plt.show()

  max_len=30
  lower_lim=25

  encoded_data_list = [sample_list for sample_list in encoded_data_list if len(sample_list)<=max_len and (len(sample_list))>=lower_lim]
  print(encoded_data_list[0:3])
  print('수강한 최대 과목수 :',max(len(sample_list) for sample_list in encoded_data_list))
  print('수강한 평균 과목수 :',sum(map(len, encoded_data_list))/len(encoded_data_list))
  plt.hist([len(sample_list) for sample_list in encoded_data_list], bins=50)
  plt.xlabel('들은 과목수(=문장 길이)')
  plt.ylabel('샘플 수(=학생 수)')
  plt.show()
  encoded_data_list_answer = [sentence[1:] for sentence in encoded_data_list]
  encoded_data_list_input = [sentence[:len(sentence)-1] for sentence in encoded_data_list]

  print("정답 label(첫 단어들만 빠졌는지 확인) = \n",encoded_data_list_answer)
  print("훈련 데이터(마지막 단어들만 빠졌는지 확인) = \n",encoded_data_list_input)

  print('문장의 최대 길이(original data) :',max(len(sentence) for sentence in encoded_data_list))
  encoded_data_list_answer_padded = pad_sequences(encoded_data_list_answer, maxlen=max_len-1,padding='post')
  encoded_data_list_input_padded = pad_sequences(encoded_data_list_input, maxlen=max_len-1,padding='post')
  print("패딩 정답 label = \n", encoded_data_list_answer_padded)
  print("패딩 훈련 label = \n", encoded_data_list_input_padded)

  return embedding_layer, vocab2idx, idx2vocab, encoded_data_list_answer_padded, encoded_data_list_input_padded

#data_preprocessing('/content/drive/MyDrive/융소_ossp_수강추천시스템DL/OSSProj_DL_sign-up-course/sample_classes.xlsx')
