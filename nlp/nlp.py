import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import re
import fasttext
import nltk
import pandas as pd
import kss
import json

model = fasttext.load_model('drive/MyDrive/Colab Notebooks/cc.ko.300.bin')
nltk.download('treebank')
nltk.download('punkt')

def plot_2d_graph(vocabs, xs, ys):
  plt.rc('font', family='NanumBarunGothic') 
  plt.figure(figsize=(8,6))
  plt.scatter(xs, ys, marker = 'o')
  for i, v in enumerate(vocabs):
    plt.annotate(v, xy = (xs[i], ys[i]))

def remove_tag(content):
   
   cleanr =re.compile('<.*?>')
   cleantext = re.sub(cleanr, '', content)

   return cleantext

def nlp(data, model):
    '''
    file_name = 'twitter_data.json'
    with open(file_name, "r") as st_json:
      data = json.load(st_json)
    '''
    data_content = []
    pre_sentence = {'코로나': ['코로나 신규 확진자가 발생했습니다'], '화재 발생': ['불 났대'], '홍수 발생': ['물이 많아'], '교통사고 발생': ['사고 났다.']}

    for record in data:
      data_content.append(record['content'])

    for index in range(len(data_content)):
      try:
        if len(data_content[index]) > 0:
          data_content[index] = pre_sentence[list(pre_sentence.keys())[list(pre_sentence.keys()).index(data_type[index])]] + kss.split_sentences(remove_tag(data_content[index]))
        else:
          data_content[index] = []
      except:
        data_content[index] = []

    content_vector = []
    index = -1

    for content in data_content:
      index = index + 1
      content_vector.append([])
      for sentence in content:
        content_vector[index].append(model.get_sentence_vector(sentence.replace('\n', '')))

    del_count = 0

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
            del_count = del_count + 1
        del  data_content[vectors][0]
      except:
        data_content[vectors] = []
      
    for index in range(len(data)):
      data[index]['content'] = data_content[index]

    return data
