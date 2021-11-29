import re

def get_content(sns_text):
    """
    한글과 띄어쓰기를 제외한 모든 부분을 제거
    두 개 이상 공백 제거
    """
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    removed = hangul.sub('', sns_text)
    return  re.sub(' +', ' ', removed) 

def dt_format(dt):
    """
    시간 형식으로 변환
    """
    if len(str(dt)) == 1:
        return f'0{str(dt)}'
    else:
        return dt

def is_valid_form(time):
    # 2021-11-22-11-22
    time_arr = time.split('-')
    # 년,월,일,시간,분 확인 
    if len(time_arr)!= 5 : 
        return False
    [year,month,day,hours,minutes] = time_arr
    # 자리수 확인
    if(len(year) !=4 or len(month) != 2 or len(day) != 2 or len(hours) != 2 or len(minutes) != 2):
        return False
    if(year.isdigit() and month.isdigit() and day.isdigit() and hours.isdigit() and minutes.isdigit()):
        return True

def delete_ObjectId(post):
    del post['_id']
    return post

def ping_form(post):
    del post['_id']
    del post['sns']
    return post