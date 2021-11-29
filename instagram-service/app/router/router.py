from flask import Blueprint,jsonify,request
from service.post_service import get_post
from service.post_service import get_ping_post
from  job.scrappe_job import scrappe
from util import is_valid_form
bp = Blueprint('main',__name__,url_prefix='/api/instagram')

@bp.route('/ping')
def ping():
    response = get_ping_post()
    return jsonify({
        "data" : response
    })
 
@bp.route('/init')
def init():
    scrappe(start_time=60*20)
    return {
        "message" : "ok"
    }

@bp.route('/data')
def get_data():
    try:
        start_date= request.args.get('start')
        end_date= request.args.get('end')
        if(not is_valid_form(start_date) or not is_valid_form(end_date)): 
            return jsonify({
            "message" :  "invalid form"
        })
        response = get_post(start_date,end_date)
        return jsonify({
            "data" : response
        })
    except Exception as e:
        print(e)
        pass