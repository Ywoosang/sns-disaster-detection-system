from sklearn.cluster import KMeans
import re
import fasttext
import pandas as pd
import kss
import json

def nlp_twitter(data): #data는 list, element: dict
  data_original_content = []
  data_content = []
  data_date = []
  data_link = []
  data_keyword = []

  pre_sentence = {'코로나': ['코로나 신규 확진자가 발생한다'], '화재': ['화재가 발생했습니다'], '홍수': ['홍수 피해가 발생한다'], '교통사고': ['사고 난다'], '폭설': ['눈이 많이 내린다'], '산불': ['산에 불이 났다'], '붕괴': ['붕괴 사고가 발생하다'], '폭발': ['폭발하다'], '태풍': ['태풍이 오다'] }

  for record in data.values():
    data_original_content.append(record['original_content'])
    data_content.append(record['content'])
    data_date.append(record['date'])
    data_link.append(record['link'])
    data_keyword.append(record['keyword'])

  data_content_all = ['코로나 신규 확진자가 발생한다', '화재가 발생했습니다', '홍수 피해가 발생한다', '사고 난다', '눈이 많이 내린다', '산에 불이 났다', '붕괴 사고가 발생하다', '폭발하다', '태풍이 오다']
  data_pre = len(data_content_all)

  for index in range(len(data_content)):
    if len(data_content[index]) > 0:
        cleaned_text = clean_text(data_content[index])
        data_content[index] = kss.split_sentences(cleaned_text)
        data_content_all = data_content_all + kss.split_sentences(cleaned_text)
    else:
        data_content[index] = []

  content_vector = []
  index = -1

  for content in data_content_all:
    content_vector.append(model.get_sentence_vector(content))

  kmeans = KMeans(n_clusters=80).fit(content_vector)

  target_label_ = []
  for i in range(data_pre):
    target_label_.append(kmeans.labels_[i])

  data_content_all_meaningful = []
  for index in range(len(data_content_all)):
    if target_label_[0] == kmeans.labels_[index] or target_label_[1] == kmeans.labels_[index] or target_label_[2] == kmeans.labels_[index] or target_label_[3] == kmeans.labels_[index] or target_label_[4] == kmeans.labels_[index] or target_label_[5] == kmeans.labels_[index] or target_label_[6] == kmeans.labels_[index] or target_label_[7] == kmeans.labels_[index] or target_label_[8] == kmeans.labels_[index]:
      if len(data_content_all[index]) >= 7:
        data_content_all_meaningful.append(data_content_all[index])

  for content in data_content:
    index = 0
    for sentence in content[:]:
      if not sentence in data_content_all_meaningful:
        content.remove(sentence)
        #content[index] = ''
      index = index + 1

  #for content in data_content:
    #print(content)

  data_result = []

  print(len(data.values()))
  print(len(data_content))

  for index in range(len(data.values())):
    try:
      if len(data_content[index]) != 0:
        data_result.append({"content": data_content[index], 'date': data_date[index], 'link': data_link[index], 'keyword': data_keyword[index], 'original_content' : data_original_content[index]})
    except:
      continue
  return data_result
