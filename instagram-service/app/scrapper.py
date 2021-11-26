from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pymysql
import re
import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import random

class InstagramCrawler:
    def __init__(self, keywords, requestTime):
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
        except Exception as error:
            self.driver.close()
            print(error)
            raise Exception('Chrome driver setting error')

    def setDriver(self):
        """
        로그인 상태의 드라이버 생성
        """
        try:
            chromedriver = "/usr/src/chrome/chromedriver"
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument('window-size=1920x1080')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("disable-gpu")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
            options.add_argument("lang=ko_KR")
            driver = webdriver.Chrome(chromedriver, options=options)
            driver = webdriver.Chrome(chromedriver)

            # 아이디, 패스워드
            userId = ['test_ywoosang', 'hyena_crawler', 'kimfe9']
            userPassword = ['test1234', 'crawler123','yhcm2618']
            # os.getenv
            driver.get('https://www.instagram.com/accounts/login')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "rgFsT"))
            )
            time.sleep(2)
            id_section = driver.find_element_by_name('username')
            id_section.clear()
            i = random.randrange(0,3)
            id_section.send_keys(userId[i])
            pw_section = driver.find_element_by_name('password')
            pw_section.clear()
            pw_section.send_keys(userPassword[i])
            pw_section.submit()
            time.sleep(3)
            self.driver = driver
        except Exception as error:
            print(error)            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument('window-size=1920x1080')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("disable-gpu")
            options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
            options.add_argument("lang=ko_KR")
            driver = webdriver.Chrome(chromedriver, options=options)
            raise Exception('driver setting error')

    def getUrl(self, word):
        """
        검색 키워드로 url 생성
        """
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
        # 모든 키워드 탐색 결과
        response = []
        for keyword in self.keywords:
            # 각각 MAX(DATE) 를 찾아서 그 이후 것들을 가져옴
            # 데이터베이스 WHERE 문으로 해당하는 MAX(DATE 찾기)
            #  try:
            #     if post["date"] <= time:
            #         continue
            #     sql = f"""
            #     INSERT INTO Post (class,link,date)
            #     VALUES ('{post["class"]}','{post["link"]}','{post["date"]}');
            #     """
            #     cursor.execute(sql)
            #     id = cursor.lastrowid
            #     for comment in post["comments"]:
            #         sql = f"""
            #         INSERT INTO Comment (postId,content)
            #         VALUES ({id},'{comment}');
            #         """
            #         # pymysql 
            #         cursor.execute(sql)
            # except:
            #     pass

            try:
                url = self.getUrl(keyword)
                self.driver.get(url)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "Nnq7C"))
                )
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()
                condition = True
                while condition:
                    post = {
                        "keyword": keyword,
                        "link": "",
                        "comments": [],
                        "date": ""
                    }
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.CLASS_NAME, "EtaWk"))
                    )
                    nextButton = self.driver.find_element_by_xpath(
                        '/html/body/div[6]/div[1]/div/div/div[2]/button')
                    html = self.driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')
                    comments = soup.select('ul.Mr508 div.C4VMK span')
                    post["link"] = self.driver.current_url
                    # 포스팅 작성 시간 조회
                    postTime = self.calcTime(soup.find('time')['datetime'])
                    # 2021-08-17-11-11
                    post["date"] = '-'.join(postTime)
                    condition = self.checkTimeValidation(
                        self.requestTime, list(map(lambda x: int(x), postTime)))
                    # 댓글 조회
                    for comment in comments:
                        print(comment.string)
                        post["comments"].append(comment.string)
                    if(len(post["comments"])):
                        print(post)
                        response.append(post)
                        #  {'class': '폭발', 'link': 'https://www.instagram.com/p/CWk9QWwDYJM/', 'comments': ['j_wonma', '😍😍 역시 에이스는 올바른 화풀이법 ㅋㅋㅋ', 'wodfriendskorea', '고생하셨습니다 👏👏', 'tooth_dkdk', 'ㅋㅋㅋㅋㅋㅋ저희가 시간 조금만 더썻으면 20개 언브로큰이었나용..?ㅎㅋㅋ', 's.in_soo', 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ저도 그래서 바머가 잘된듯요😂😂', '0hohoho0', '오 ㅋㅋ👏👏👏👏👏', '_m_ssang', '행님 고생하셨습니다👏👏👏👏', 'sorossfit', '고생하셨습니다!! 역시 잘하십니당🔥', 'cf_bum', '잘해~~김사장', 'byeol_papa', 'ㅋㅋ 노총각 이렇게라도 풀어야져 잘했네'], 'date': '2021-11-22-12-04'}
                        # 여기서 각 Post 마다 Insert 
                        # 각 class 마다 최근 시간 이후 크롤링
                    time.sleep(5)
                    nextButton.click()
                # 현재 키워드 탐색 결과 추가
                time.sleep(2)
            except Exception as error:
                print(error)
                self.driver.close()
                return
        print(response)
        return response
    
async def crawl():
    try:
        keywords = ['산불','교통사고','붕괴','폭발','화재']
        # schedule.every(10).minutes.do(getData())
        # 가장 최신 포스트 시간 가져오기
        db = pymysql.connect(
            host="127.0.0.1",
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
    
class SchedulerService:
    def start(self):
        self.sch = AsyncIOScheduler()
        self.sch.start()
        self.sch.add_job(crawl, 'interval', seconds=900, max_instances=1)
        
a = SchedulerService()
a.start()