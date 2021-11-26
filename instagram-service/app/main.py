import pymysql
import json
import re
from collections import OrderedDict

start_date='2021-11-26-02-00'
end_date='2021-11-28-00-00'
db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="1234",
        db="Instagram",
        charset="utf8mb4")
 
cursor = db.cursor()
sql = f"""SELECT P.date,P.link,P.keyword,C.content FROM Post P 
        LEFT JOIN Comment C 
        ON C.postId = P.id
        WHERE P.date > '{start_date}' AND P.date <= '{end_date}'
        ORDER BY P.date DESC"""
cursor.execute(sql)
rows = cursor.fetchall()


#({post["keyword"]}','{post["link"]}','{post["date"]}')


response = [] 

for row in rows:
    content = re.sub(r'\n', '', hangul.sub('', row[3])) # 한글과 띄어쓰기를 제외한 모든 부분을 제거
    if content == '':
        continue
    date = row[0]
    link = row[1]
    keyword = row[2]
    sns = row[3]
    service = 'instagram'
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+') # 한글과 띄어쓰기를 제외한 모든 글자
    
    response.append({
        "link" : link,
        "sns" : sns,
        "service": service,
        "keyword" : keyword,
        "content" : content,
        "date" : date
    })
print(response)
print('length of res',len(response))
db.close()