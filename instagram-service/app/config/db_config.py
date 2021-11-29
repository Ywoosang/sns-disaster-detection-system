import pymongo

# mongodb 접속
mongodb_uri = "mongodb://instagram-db:27020/"
conn = pymongo.MongoClient(mongodb_uri)
# 데이터베이스 생성하거나 기존것 사용
db = conn.nlp_model