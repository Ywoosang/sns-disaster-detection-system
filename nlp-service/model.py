import kss
from sklearn.cluster import KMeans
from util import clean_text
import time
import re
import numpy as np
 
def nlp(data,model): #data는 list, element: dict
  file_path = "fword_list.txt"

  with open(file_path) as f:
      ban_words = f.readlines()

  ban_words = [line.rstrip('\n') for line in ban_words]

  start = time.time()
  if len(data) <= 20:
      print("[Error] Too little data to learn", '데이터 수: ' , len(data))
      return data
   
  data_service = []
  data_content = []
  data_date = []
  data_link = []
  data_keyword = []
  data_sns = []
  for record in data:
    for ban_word in ban_words:
      if ban_word not in record['content']:
        if record['content'] not in data_content:
          data_service.append(record['service'])
          data_content.append(record['content'])
          data_date.append(record['date'])
          data_link.append(record['link'])
          data_keyword.append(record['keyword'])
          data_sns.append(record['sns'])
    

  data_content_all = ['코로나 신규 확진자가 발생했다.', '화재가 발생했다.', '홍수 피해가 index발생했다.', '사고 났다.', '눈이 많이 내린다.', '산에 불이 났다.', '붕괴 사고가 발생하다.', '폭발하다.', '태풍이 발생했다.']
  data_pre = len(data_content_all)

  for index in range(len(data_content)):
    if len(data_content[index]) > 0:
        cleaned_text = clean_text(data_content[index])
        data_content[index] = kss.split_sentences(cleaned_text)
        data_content_all = data_content_all + kss.split_sentences(cleaned_text)
        print("{}/{}".format(index, len(data)))
    else:
        print("{}/{}".format(index, len(data)))
        data_content[index] = []

  content_vector = []
  index = -1

  for content in data_content_all:
    content_vector.append(model.get_sentence_vector(content))

  if len(content_vector) > 200:
    kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
  elif len(content_vector)  > 50:
    kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
  elif len(content_vector)  > 21:
    kmeans = KMeans(n_clusters=10, init='k-means++').fit(content_vector)
    
  target_label_ = []
  for i in range(data_pre):
    target_label_.append(kmeans.labels_[i])

  data_content_all_meaningful = []
  for index in range(len(data_content_all)):
    if target_label_[0] == kmeans.labels_[index] or target_label_[1] == kmeans.labels_[index] or target_label_[2] == kmeans.labels_[index] or target_label_[3] == kmeans.labels_[index] or target_label_[4] == kmeans.labels_[index] or target_label_[5] == kmeans.labels_[index] or target_label_[6] == kmeans.labels_[index] or target_label_[7] == kmeans.labels_[index] or target_label_[8] == kmeans.labels_[index]:
      if len(data_content_all[index]) >= 7:
        data_content_all_meaningful.append(data_content_all[index])
        print('Append meaningful data')

  for sentence in data_content_all_meaningful[:]:
    for ban_word in ban_words:
      if ban_word in sentence and sentence in data_content_all_meaningful:
        data_content_all_meaningful.remove(sentence)
        print('Delete ban words')

  print('data_content_all_meaningful:', len(data_content_all_meaningful) - 7)
  for content in data_content:
    for sentence in content[:]:
      if sentence not in data_content_all_meaningful:
        content.remove(sentence)
        
  data_result = []
  count = 0
  for index in range(len(data)):
    if len(data_content[index]) != 0:
      data_sentence = ''
      for sentence in data_content[index]:
          data_sentence += sentence + '. '
          count = count + 1
          print(count)

      data_result.append({ "service": data_service[index],
                          "keyword": data_keyword[index],
                          "link": data_link[index],
                          "sns": data_sns[index],
                          "content": data_sentence, 
                          'date': data_date[index]})
      print('append result')
  print('data result:', len(data_result))
  print("----------------------------------------------------------------------------------------")
  print("모델 학습 시간 :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
  return data_result
