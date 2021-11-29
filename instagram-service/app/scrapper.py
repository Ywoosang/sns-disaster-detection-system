 # 셀레니움
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# bs4 
from bs4 import BeautifulSoup
# 시간지연 
import time
# 인스타 secret 랜덤값
import random
# 데이터베이스
import pymongo
# 전처리
from util import get_content
from util import dt_format
import re 
# 시간 설정
from datetime import datetime
from datetime import timedelta 
from dateutil.tz import gettz
from config.db_config import db

class InstagramCrawler:
    def __init__(self, keywords, index,start_time=None):
        self.keywords = keywords
        self.userId = ['test_ywoosang', 'kimfe9', 'ninei_yat','Hong_test1','eses20010427','so_omin0703']
        self.userPassword = ['test1234','yhcm2618','ninei1234','testtest123','nonochadan','chadannono']
        self.index = index
        self.start_time = start_time

    def run(self):
        """
        스크래핑 시작
        """
        is_driver = self.setDriver()
        if(is_driver):
            response = self.getComments()
            return response
        else:
            print('실패')
            return []

    def setDriver(self):
        """
        로그인 상태의 드라이버 생성
        """
        time.sleep(2)
        options = Options()
        # options.add_argument('headless')
        options.add_argument('--start-fullscreen')
        options.add_argument('window-size=1920x1080') 
        options.add_argument("disable-gpu")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
        driver = webdriver.Chrome('/home/ywoosang/바탕화면/개인공부/오픈소스/SNS-Disaster-Detection-System/instagram-service/app/chromedriver',options=options)
        driver.get('https://www.instagram.com/?hl=ko')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "rgFsT"))
        )
        time.sleep(2)
        id_section = driver.find_element_by_name('username')
        id_section.clear()
        time.sleep(1)
        # id_section.send_keys(self.userId[self.index])
        id_section.send_keys('test_ywoosang')
        pw_section = driver.find_element_by_name('password')
        pw_section.clear()
        pw_section.send_keys('test1234')
        # pw_section.send_keys(self.userPassword[self.index])
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        time.sleep(7)
        # 로그인창으로 나왔는지 확인
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        is_ok = soup.select_one("main > div > div > div > section > div > button")

        is_fail = soup.select_one("#loginForm > div > div:nth-child(1) > div > label > input")
        if not is_ok:
            print('로그인 실패')
            id_section = driver.find_element_by_name('username')
            id_section.clear()
            time.sleep(1)
            # id_section.send_keys(self.userId[self.index])
            id_section.send_keys('ninei_yat')
            pw_section = driver.find_element_by_name('password')
            pw_section.clear()
            pw_section.send_keys('ninei1234')
            # pw_section.send_keys(self.userPassword[self.index])
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
            time.sleep(7)
            print(is_fail)
            return False
        self.driver = driver
        return True
    def getUrl(self, word):
        """
        검색 키워드로 url 생성
        """
        if(word == '코로나'):
            word = '코로나확진'
        url = f'https://www.instagram.com/explore/tags/{word}'
        return url

    def calcTime(self, time):
        """
        시간 문자열을 받아 년,월,일,시,분 을 리스트로 만들어 반환
        """
        [year, month] = time.split('-')[:2]
        day = time.split('-')[-1].split('T')[0]
        [hour, minute] = time.split('-')[-1].split('T')[-1].split(':')[:2]
        return [year, month, day, hour, minute]

    def checkTimeValidation(self, requestTime, postTime):
        """
        게시물 작성 시간이 요청 시간 이후인지 여부 반환
        ex) 요청시간이 2021 11 10 00 00 이라면 게시물 작성 시간이 그 이후인지
        """
        for index in list(range(len(requestTime))):
            if requestTime[index] > postTime[index]:
                return False
            elif requestTime[index] < postTime[index]:
                return True
        return False

    def getComments(self):
        """
        모든 키워드 탐색 결과
        로그인된 하나의 드라이버로 모든 키워드 탐색
        """
        for keyword in self.keywords:
            print(self.start_time,'분 이후')
            if self.start_time == None:
                minutes = 30
            else:
                minutes = self.start_time
            ### 스케줄러 시간 설정 
            end_datetime = datetime.now(gettz('Asia/Seoul')) + timedelta(minutes= 0)
            start_datetime = end_datetime + timedelta(minutes= -minutes)
            startTime = f"{dt_format(start_datetime.year)}-{dt_format(start_datetime.month)}-{dt_format(start_datetime.day)}-{dt_format(start_datetime.hour)}-{dt_format(start_datetime.minute)}"
            print('시작 시간',startTime)
            request_time = startTime.split('-')
            # 검색할 URL 
            url = self.getUrl(keyword)
            # 키워드 url 로 넘어가기
            self.driver.get(url)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Nnq7C"))
            )
            time.sleep(1)
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()
            condition = True
            collection = db.post 
            while condition:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "EtaWk"))
                )
                nextButton = self.driver.find_element_by_xpath(
                    '/html/body/div[6]/div[1]/div/div/div[2]/button')
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                # 글 본문
                main_text = soup.select_one('div.EtaWk div.ZyFrc div.C4VMK > span')

                # 링크, 시간
                comments = soup.select('ul.Mr508 div.C4VMK span')
                print(self.driver.current_url)
                post_link = self.driver.current_url
                postTime = self.calcTime(soup.find('time')['datetime'])
                post_date = '-'.join(postTime)

                # 댓글 혹은 글 본문 
                condition = self.checkTimeValidation( list(map(lambda x: int(x),request_time)), list(map(lambda x: int(x), postTime)))
                if(not condition):
                    break;
                
                # 포스트 본문 db 저장
                if main_text != None:
                    sns = re.sub('<.+?>', '', str(main_text), 0).strip() 
                    sns.split("#")[0] 
                    content = get_content(sns)
                print(content)
                collection.insert_one({
                    "service" : "instagram",
                    "content" : content,
                    "sns" : sns,
                    "link" :post_link,
                    "date" : post_date,
                    "keyword" : keyword
                })

                # 댓글 본문 db 저장
                for comment in comments:
                    if comment == None:
                        continue
                    comment = comment.string
                    content = get_content(comment)
                    print(content)
                    collection.insert_one({
                    "service" : "instagram",
                    "content" : content,
                    "sns" : comment,
                    "link" :post_link,
                    "date" : post_date,
                    "keyword" : keyword
                })
                sleepTime = random.uniform(1, 3)
                sleepTime = round(sleepTime, 2)
                time.sleep(sleepTime)
                nextButton.click()
        self.driver.close()