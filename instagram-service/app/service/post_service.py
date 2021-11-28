import pymysql
import re

def get_post(start_date,end_date):
    db = pymysql.connect(
            host="instagram-database",
            port=3306,
            user="root",
            passwd="1234",
            db="Instagram",
            charset="utf8mb4"
    )
    cursor = db.cursor()
    sql = f"""SELECT P.date,P.link,P.keyword,C.content FROM Post P 
            LEFT JOIN Comment C 
            ON C.postId = P.id
            WHERE P.date > '{start_date}' AND P.date <= '{end_date}'
            ORDER BY P.date DESC"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    dataset = []
    for row in rows:
        # 한글과 띄어쓰기를 제외한 모든 글자
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  
        # 한글과 띄어쓰기를 제외한 모든 부분을 제거 
        content = re.sub(r'\n', '', hangul.sub('', row[3]))  
        if content == '' or content == None:
            continue
        date = row[0]
        link = row[1]
        keyword = row[2]
        sns = row[3]
        service = 'instagram'
        data = {
            "link" : link,
            "sns" : sns,
            "service": service,
            "keyword" : keyword,
            "content" : content,
            "date" : date
        }
        if data not in dataset:
            dataset.append(data)
    return dataset
        