import pymysql
import re
from flask import Flask, request
from  flask_apscheduler import APScheduler
from scrapper import InstagramCrawler

app = Flask(__name__)
scheduler = APScheduler()
   
async def crawl():
    try:
        keywords = ['산불','교통사고','붕괴','폭발','화재']
        # schedule.every(10).minutes.do(getData())
        # 가장 최신 포스트 시간 가져오기
        db = pymysql.connect(
            host="instagram-database",
            port=3306,
            user="root",
            passwd="1234",
            db="Instagram",
            charset="utf8mb4"
        )
        cursor = db.cursor()
        for keyword in keywords:
            sql = f"""
            SELECT MAX(date) FROM Post WHERE keyword='{keyword}';
            """
            cursor.execute(sql)
            row = cursor.fetchone()
            time = None
            if row[0] is None:
                # DB 에 아무 데이터도 없을 때 하루 전날로 설정하는 코드
                # datetime
                time = '2021-11-26-18-10'
            else:
                time = row[0] 
            date = time.split('-')
            keyword = [keyword]
            crawler = InstagramCrawler(keyword, list(map(lambda x: int(x), date)))
            response = crawler.run()
            for post in response:
                try:
                    if post["date"] <= time:
                        continue
                    sql = f"""
                    INSERT INTO Post (keyword,link,date)
                    VALUES ('{post["keyword"]}','{post["link"]}','{post["date"]}');
                    """
                    cursor.execute(sql)
                    id = cursor.lastrowid
                    for comment in post["comments"]:
                        sql = f"""
                        INSERT INTO Comment (postId,content)
                        VALUES ({id},'{comment}');
                        """
                        # pymysql 
                        cursor.execute(sql)
                except:
                    pass

            db.commit()
        db.close()
        return {
            "msg": "ok"
        }
    except Exception as error:
        print(error)
        return {
            "error": error
        }

@app.route('/api/instagram/data')
def get_data():
    try:
        start_date= request.args.get('start')
        end_date= request.args.get('end')
        # 검증 코드 구현할 것
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
    except Exception as e:
        print(e)
        pass


if __name__ == '__main__':
    scheduler.add_job(id="Scheduled task",func = crawl, trigger = 'interval',seconds=60*10)
    scheduler.start()
    app.run(host ='0.0.0.0',port=8000)