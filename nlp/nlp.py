from sklearn.cluster import KMeans
import re
import fasttext
import pandas as pd
import kss
import json

def remove_tag(content):
   
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)

   return cleantext

model_dir = ''

model = fasttext.load_model(model_dir)

def nlp(data, model = fasttext.load_model(model_dir)):

    # .json파일일 경우 주석 제거
    '''
    file_name = 'twitterdata-1.json'
    with open(file_name, "r") as st_json:
      data = json.load(st_json)
    '''

    data_content = []
    data_date = []
    data_link = []
    data_type = []

    pre_sentence = {'코로나': ['코로나 신규 확진자가 발생했습니다'], '화재': ['불 났대'], '홍수': ['물이 많아'], '교통사고': ['사고 났다'], '폭설': ['눈이 많이 왔습니다'], '산불': ['산에 불이 발생했습니다'], '붕괴': ['붕괴 사고가 발생했습니다'], '폭발': ['폭발 했습니다'], '태풍': ['태풍이 옵니다'] }

    for record in data:
      data_content.append(record['content'])
      data_date.append(record['date'])
      data_link.append(record['link'])
      data_type.append(record['type'])

    for index in range(len(data_content)):
      if len(data_content[index]) > 0:
          data_content[index] = pre_sentence[list(pre_sentence.keys())[list(pre_sentence.keys()).index(data_type[index])]] + kss.split_sentences(remove_tag(data_content[index]))
      else:
          data_content[index] = []

    content_vector = []
    index = -1

    for content in data_content:
      index = index + 1
      content_vector.append([])
      for sentence in content:
        content_vector[index].append(model.get_sentence_vector(sentence.replace('\n', '')))

    for vectors in range(len(content_vector)):
      try:
        if len(content_vector[vectors]) >= 5:
          kmeans = KMeans(n_clusters=5).fit(content_vector[vectors])
        elif len(content_vector[vectors]) >= 4:
          kmeans = KMeans(n_clusters=4).fit(content_vector[vectors])
        elif len(content_vector[vectors]) >= 3:
          kmeans = KMeans(n_clusters=3).fit(content_vector[vectors])
        else:
          kmeans = KMeans(n_clusters=2).fit(content_vector[vectors])

        target_label = kmeans.labels_[0]

        for index in range(len(data_content[vectors])):
          if index >= len(data_content[vectors]):
            break
          if kmeans.labels_[index] != target_label:
            del data_content[vectors][index]
        del  data_content[vectors][0]
      except:
        data_content[vectors] = []

    for index in range(len(data)):
      data[index]['content'] = data_content[index] 

   return data
