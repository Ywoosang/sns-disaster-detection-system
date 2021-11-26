from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
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
            print(error)            
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
                    postTime = self.calcTime(soup.find('time')['datetime'])
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
                    time.sleep(3)
                    nextButton.click()
                # 현재 키워드 탐색 결과 추가
                time.sleep(2)
            except Exception as error:
                print(error)
                self.driver.close()
                return
        print(response)
        return response