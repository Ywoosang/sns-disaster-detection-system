from flask import Blueprint,jsonify,request
import pymysql
from service.post_service import get_post
from  job.scrappe_job import scrappe

bp = Blueprint('main',__name__,url_prefix='/api/instagram')

@bp.route('/ping')
def ping():
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
            ORDER BY P.date DESC
            LIMIT 20"""
    cursor.execute(sql)
    rows = cursor.fetchall()
    response = []
    for row in rows:
        date = row[0]
        link = row[1]
        keyword = row[2] 
        content = row[3]
        response.append({
            "link" : link,
            "service": "instagram",
            "content" : content,
            "keyword" : keyword,
            "date" : date
        })
    db.close()
    return jsonify({
        "data" : response
        })
 
@bp.route('/init')
def init():
    scrappe()
    return {
        "message" : "ok"
    }

@bp.route('/data')
def get_data():
    try:
        start_date= request.args.get('start')
        end_date= request.args.get('end')
        # 검증 코드 구현할 것
        response = getInstagram_post(start_date,end_date)
        print(f': Response Length {len(response)}')
        return jsonify({
            "data" : response
        })
    except Exception as e:
        print(e)
        pass