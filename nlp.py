from sklearn.cluster import KMeans
import re
import fasttext
import pandas as pd
import kss
import json

model = fasttext.load_model('drive/MyDrive/Colab Notebooks/cc.ko.300.bin')

def clean_text(text):
    cleaned_text = re.sub('[a-zA-z]','',text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"\♥\♡\ㅋ\ㅠ\ㅜ\ㄱ\ㅎ\ㄲ\ㅡ]','',cleaned_text)
    cleaned_text = re.sub('<.*?>', '', cleaned_text)

    return cleaned_text

#file_name = 'twitterdata-1.json'
#with open(file_name, "r") as st_json:
  #data = json.load(st_json)

def nlp(data): #data는 list, element: dict
  data_service = []
  data_content = []
  data_date = []
  data_link = []
  data_keyword = []
  data_sns = []

  pre_sentence = {'코로나': ['코로나 신규 확진자가 발생한다'], '화재': ['화재가 발생했습니다'], '홍수': ['홍수 피해가 발생한다'], '교통사고': ['사고 난다'], '폭설': ['눈이 많이 내린다'], '산불': ['산에 불이 났다'], '붕괴': ['붕괴 사고가 발생하다'], '폭발': ['폭발하다'], '태풍': ['태풍이 오다'] }

  for record in data:
    data_service.append(record['service'])
    data_content.append(record['content'])
    data_date.append(record['date'])
    data_link.append(record['link'])
    data_keyword.append(record['keyword'])
    data_sns.append(record['sns'])

  #data_content_all = ['코로나 신규 확진자가 발생한다', '화재가 발생히여 피해가 발생했습니다.', '홍수 피해가 발생한다', '사고가 발생해 피해가 발생했습니다.', '눈이 많이 내려 마비되고 있습니다.', '산에 불이나 피해가 발생하고 있습니다.', '붕괴 사고가 발생하여 피해가 발생했습니다.', '폭발사고가 발생하여 피해가 발생했습니다.', '태풍이 오고 있으니 주의하시기 바랍니다.']
  data_content_all = ['코로나 신규 확진자가 발생했다.', '화재가 발생했다.', '홍수 피해가 발생했다.', '사고 났다.', '눈이 많이 내린다.', '산에 불이 났다.', '붕괴 사고가 발생하다.', '폭발하다.', '태풍이 발생했다.']
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

  kmeans = KMeans(n_clusters=120).fit(content_vector)

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

  for content in data_content:
    print(content)

  data_result = []

  for index in range(len(data)):
    if len(data_content[index]) != 0:
      data_result.append({ "service": data_service[index],
                          "keyword": data_keyword[index],
                          "link": data_link[index],
                          "sns": data_sns[index]
                          "content": data_content[index], 
                          'date': data_date[index]})
  return data_result
