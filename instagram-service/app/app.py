from flask import Flask 
from flask_cors import CORS
import pymysql
def create_app():
    app = Flask(__name__)
    CORS(app)
    # JSON 한글 깨짐 방지
    app.config['JSON_AS_ASCII'] = False
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="1234",
        charset="utf8mb4"
    )
    cursor = db.cursor()
    sql = """CREATE DATABASE IF NOT EXISTS Instagram DEFAULT  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"""
    cursor.execute(sql)
    sql = """USE Instagram;"""
    cursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS Post (
                id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
                keyword VARCHAR(20) NOT NULL,
                link VARCHAR(300) NOT NULL,
                date VARCHAR(50) NOT NULL,
                PRIMARY KEY(id)
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"""
    cursor.execute(sql)
    sql = """CREATE TABLE IF NOT EXISTS Comment (
                id INT(11) UNSIGNED NOT NULL AUTO_INCREMENT,
                postId INT(11) UNSIGNED NOT NULL,
                content TEXT,
                FOREIGN KEY (postId) REFERENCES Post(id) ON DELETE CASCADE,
                PRIMARY KEY(id)
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; """
    cursor.execute(sql)
    db.commit()
    db.close()
    # @app.before_request
    # def before_request():
    #     g.db =  pymysql.connect(
    #         host="instagram-database",
    #         port=3306,
    #         user="root",
    #         passwd="1234",
    #         db="Instagram",
    #         charset="utf8mb4"
    #     )


    from router import router
    app.register_blueprint(router.bp)
    return app
