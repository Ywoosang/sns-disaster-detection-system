import pymysql
import time as timeChecker
import sys
sys.path.append('..')
import scrapper


def scrappe():
    keywords = [ '교통사고','코로나','화재','폭설']
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
    now = timeChecker.localtime()
    index = now.tm_min // 10
    for keyword in keywords:
        # 키워드 출력
        print(keyword) 
        sql = f"""
        SELECT MAX(date) FROM Post WHERE keyword='{keyword}';
        """
        cursor.execute(sql)
        row = cursor.fetchone()
        time = None
        if row[0] is None:
            # DB 에 아무 데이터도 없을 때 하루 전날로 설정
            time = '2021-11-27-18-10'
        else:
            time = row[0]
        date = time.split('-')
        try:
            crawler = scrapper.InstagramCrawler(keyword, list(map(lambda x: int(x), date)),index)
            response = crawler.run()
            index = (index + 1) % 7
            for post in response:
                try:
                    # 이미 존재하는 글이거나 시작 시간 이전에 작성된 글일 경우 
                    if post["date"] <= time:
                        continue
                    sql = f"""
                    INSERT INTO Post (keyword,link,date)
                    VALUES ('{post["keyword"]}','{post["link"]}','{post["date"]}');
                    """
                    cursor.execute(sql)
                    id = cursor.lastrowid
                    for comment in post["comments"]:
                        if comment:
                            continue
                        sql = f"""
                        INSERT INTO Comment (postId,content)
                        VALUES ({id},'{comment}');
                        """
                        # pymysql 
                        cursor.execute(sql)
                        db.commit()
                except Exception as e:
                    print(e)
            db.close()
        except Exception as e:
            print(e)
            continue
     