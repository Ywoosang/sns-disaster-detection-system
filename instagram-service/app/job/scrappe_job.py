import pymysql
import time as timeChecker
import sys
sys.path.append('..')
import scrapper


def scrappe(start_time=None):
    try:
        keywords = [ '교통사고','코로나','화재','폭설']
        # schedule.every(10).minutes.do(getData())
        # 가장 최신 포스트 시간 가져오기
        now = timeChecker.localtime()
        index = now.tm_min // 10
        # 크롤링 시작
        crawler = scrapper.InstagramCrawler(keywords,index,start_time=start_time)
        crawler.run()
    except Exception as e:
        print(e)
