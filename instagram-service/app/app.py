from flask import Flask 
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    # JSON 한글 깨짐 방지
    app.config['JSON_AS_ASCII'] = False
    from router import router
    app.register_blueprint(router.bp)
    return app
