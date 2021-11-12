import uvicorn
from fastapi import FastAPI
from fastapi import Body, FastAPI, status
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import time
from typing import List
import pymysql
 
app = FastAPI()


class InstagramCrawler:
    def __init__(self,keywords:List[str],requestTime: List[int]):
        self.keywords = keywords
        self.requestTime = requestTime

    def run(self):
        """
        스크래핑 시작
        """
        try:
            self.setDriver()
            response = self.getComments()
            self.driver.close()
            return response
        except  Exception as error:
            self.driver.close()
            print(error)
            raise Exception('Chrome driver setting error')

    def setDriver(self):
        """
        로그인 상태의 드라이버 생성
        """
        try:
            chromedriver = "/home/ywoosang/바탕화면/개인공부/오픈소스/해커톤/instagram/app/chromedriver"
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=1920x1080')
            options.add_argument("disable-gpu")
            options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
            options.add_argument("lang=ko_KR")
            driver = webdriver.Chrome(chromedriver,options=options)
            # userId = 'test_ywoosang'
            # userPassword = 'test1234'        
            userId = '_ywoosang'
            userPassword = 'bodu3717@@'   
            driver.get('https://www.instagram.com/accounts/login')
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "rgFsT"))
            )
            time.sleep(2)
            id_section = driver.find_element_by_name('username')
            id_section.clear()
            id_section.send_keys(userId)
            pw_section = driver.find_element_by_name('password')
            pw_section.clear()
            pw_section.send_keys(userPassword)
            pw_section.submit()
            time.sleep(3)
            self.driver = driver
        except  Exception as error:
            print(error)
            raise Exception('driver setting error')

    def getUrl(self,word):
        """
        검색 키워드로 url 생성
        """
        url = f'https://www.instagram.com/explore/tags/{word}'
        return url

    def calcTime(self,time) -> List[int]:
        """
        시간 문자열을 받아 년,월,일,시,분 을 리스트로 만들어 반환
        """
        [year,month] = time.split('-')[:2]
        day = time.split('-')[-1].split('T')[0]
        [hour,minute] = time.split('-')[-1].split('T')[-1].split(':')[:2]
        return [year,month,day,hour,minute]

    def checkTimeValidation(self,requestTime:List[int],postTime: List[int]):
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
        # 모든 키워드 탐색 결과
        response = []
        for keyword in self.keywords:
            try:
                url = self.getUrl(keyword)
                self.driver.get(url)
                WebDriverWait(self.driver,10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Nnq7C"))
                )
                self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()
                condition = True 
                while condition:
                    post = {
                        "class":keyword,
                        "link": "",
                        "comments" : [],
                        "date" : ""
                    }
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "EtaWk"))
                    )
                    nextButton = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button')
                    html = self.driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    comments = soup.select('ul.Mr508 div.C4VMK span')
                    post["link"] = self.driver.current_url
                    # 포스팅 작성 시간 조회
                    postTime = self.calcTime(soup.find('time')['datetime'])
                    post["date"] = '-'.join(postTime)
                    condition = self.checkTimeValidation(self.requestTime,list(map(lambda x: int(x),postTime)))
                    # 댓글 조회
                    for comment in comments:
                        print(comment.string)
                        post["comments"].append(comment.string)
                    if(len(post["comments"])):
                        print(post)
                        response.append(post)
                    nextButton.click()
                # 현재 키워드 탐색 결과 추가
                time.sleep(1)
            except Exception as error:
                    print(error)
                    self.driver.close()
                    return;
        print(response)
        return response

@app.get('/api/instagram/data/')
async def connectionTest():
    try:
        db = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="1234",
            db="Instagram",
            charset="utf8mb4"
        )    
        cursor = db.cursor()
        sql = """
        SELECT P.date,P.link,P.class,C.content FROM Post P 
        LEFT JOIN Comment C 
        ON C.postId = P.id
        ORDER BY P.date DESC;
        """
        cursor.execute(sql)
        dataset = cursor.fetchall()
        sql = """"""
        db.close()
        response = []
        for data in dataset:
            response.append({
                "date": data[0],
                "link": data[1],
                "class":data[2],
                "content": data[3] 
            })
        return {
            "data" : response,
        }
    except Exception as error:
        print(error)
        return {
            "error" : "connectin error"
        }


@app.get('/api/instagram/data/1')
async def postData():
    try:
        db = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="1234",
            db="Instagram",
            charset="utf8mb4"  
        )  
        cursor = db.cursor()
        sql = """
        SELECT MAX(date) FROM Post;
        """
        cursor.execute(sql) 
        row = cursor.fetchone()
        time = None
        if row[0] is None:
            time = '2021-11-10-11-10'
        else:
            time = row[0] 
        keywords = ['산불','교통사고','붕괴','폭발','화재']
        date = time.split('-')
        crawler= InstagramCrawler(keywords,list(map(lambda x: int(x),date)))
        response = crawler.run()
        for post in response:
            if post["date"] <= time:
                continue
            sql = f"""
            INSERT INTO Post (class,link,date)
            VALUES ('{post["class"]}','{post["link"]}','{post["date"]}');
            """
            cursor.execute(sql)
            id = cursor.lastrowid
            for comment in post["comments"]:
                sql = f"""
                INSERT INTO Comment (postId,content)
                VALUES ({id},'{comment}');
                """
                cursor.execute(sql)
        db.commit()
        db.close()
        return {
            "msg" : "ok"
        }
    except Exception as error:
        print(error)
        return {
            "error" : error
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 