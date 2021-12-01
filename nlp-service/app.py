from flask import (
    Flask,
    jsonify,
    request,
)
from  flask_apscheduler import APScheduler
import requests
from datetime import datetime
from dateutil.tz import gettz
from datetime import timedelta
from util import dt_format
from model import nlp
import fasttext
import pymongo
from util import is_valid_form
from util import delete_ObjectId
from util import ping_form
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
scheduler = APScheduler()

# 모델 로드
model_dir = '/usr/src/cc.ko.300.bin'
model = fasttext.load_model(model_dir)

# mongodb 접속
mongodb_uri = "mongodb://nlp-db:27017/"
conn = pymongo.MongoClient(mongodb_uri)
# create or use
db = conn.nlp_model
# collection 생성 

@app.route("/api/model/data")
def get_data():
    start_date= request.args.get('start')
    end_date= request.args.get('end')
    if(not is_valid_form(start_date) or not is_valid_form(end_date)): 
        return jsonify({
        "message" :  "invalid form"
        })
    collection = db.post
    posts = collection.find({
        "date": {
            "$lte": str(end_date),
            "$gt": str(start_date)
        }
    }).sort('date',pymongo.DESCENDING)
    dataset = list(map(delete_ObjectId,list(posts)))
    response = []
    for data in dataset:
        if data not in response:
            response.append(data) 
    return jsonify({
        "data" : response
    })

@app.route("/api/model/ping")
def ping():
    collection = db.post
    posts = collection.find().sort('date',pymongo.DESCENDING).limit(20)
    dataset = list(map(ping_form,list(posts)))
    response = []
    for data in dataset:
        if data not in response:
            response.append(data) 
    return jsonify({
        "data" : response
    })


@app.route("/api/model/init",methods=["POST"])
def fit():
    scheduledTask(number=200,minutes=10000)
    return jsonify({
        "data" : "ok"
    })

def scheduledTask(number=160,minutes=30):
    print('학습할 데이터 최대 개수 지정:',number)
    urls = [
        "http://naver-service:3001/api/naver/data",
        "http://twitter-service:3002/api/twitter/data",
        # "http://instagram-service:8000/api/instagram/data"
    ]
    # 16-31
    # 16-21
    end_datetime = datetime.now(gettz('Asia/Seoul')) + timedelta(minutes= 0)
    start_datetime = end_datetime + timedelta(minutes= -minutes)
    # request query params
    start = f"{dt_format(start_datetime.year)}-{dt_format(start_datetime.month)}-{dt_format(start_datetime.day)}-{dt_format(start_datetime.hour)}-{dt_format(start_datetime.minute)}"
    end = f"{dt_format(end_datetime.year)}-{dt_format(end_datetime.month)}-{dt_format(end_datetime.day)}-{dt_format(end_datetime.hour)}-{dt_format(end_datetime.minute)}"
    params = { 'start': start,'end': end}
    dataset = []
    try:
        for url in urls:
            response = requests.get(url,params=params).json()
            if response.get('data'):
                for data in response['data']:
                    dataset.append(data)
        scrapped_number = len(dataset)
        print('데이터셋 개수:',scrapped_number)
        dataset_naver = []
        dataset_twitter = []
        dataset_instargram = []

        for element in dataset:
            if element['service'] == 'naver':
                dataset_naver.append(element)
            if element['service'] == 'twitter':
                dataset_twitter.append(element)
            elif element['service'] == 'instagram':
                dataset_instargram.append(element)
        dataset = dataset_twitter + dataset_instargram + dataset_naver
        
        if len(dataset) > number:
            if len(dataset_instargram) >= int(number/4) and len(dataset_twitter) >= int(number/4) and len(dataset_naver) >= int(number/2) and:
                dataset = random.sample(dataset_instargram,int(number/4)) + random.sample(dataset_twitter,int(number/4)) + random.sample(dataset_naver,int(number/2))
            elif len(dataset_twitter) >= int(number/7) and len(dataset_naver) >= int(number/3) and:
                dataset = random.sample(dataset_twitter,int(number/7)) + random.sample(dataset_naver,int(number/3))
            else:
                dataset = random.sample(dataset,number)
            
        trained_dataset = nlp(dataset,model)
        trained_number = len(trained_dataset)
        print('학습된 데이터 개수',trained_number)
        collection = db.post
        for post in trained_dataset:
            collection.insert_one(post)
    except Exception as e:
        print(e)
   

if __name__ == '__main__':
    scheduler.add_job(id="Scheduled task",func = scheduledTask, trigger = 'interval',seconds=30*60)
    scheduler.start()
    app.run(host ='0.0.0.0',port=5000)
