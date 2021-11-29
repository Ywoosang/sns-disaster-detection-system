import re

def clean_text(text):
    cleaned_text = re.sub('[a-zA-z]','',text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"\♥\♡\ㅋ\ㅠ\ㅜ\ㄱ\ㅎ\ㄲ\ㅡ]','',cleaned_text)
    cleaned_text = re.sub('<.*?>', '', cleaned_text)
    return cleaned_text


def dt_format(dt):
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
