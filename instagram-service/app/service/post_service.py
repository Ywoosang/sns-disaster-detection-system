from config.db_config import db
import pymongo
from util import delete_ObjectId
from util import ping_form

def get_post(start_date,end_date):
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
    return response


def get_ping_post():
    collection = db.post
    posts = collection.find().sort('date',pymongo.DESCENDING).limit(20)
    dataset = list(map(ping_form,list(posts)))
    response = []
    for data in dataset:
        if data not in response:
            response.append(data) 
    return response