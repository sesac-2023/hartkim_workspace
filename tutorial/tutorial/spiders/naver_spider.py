# 경제-부동산 뉴스기사 URL
BASE_URL = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=260&sid1=101&date={}}&page={}'
# data 양식 20230807
# page 양식


import scrapy

from datetime import datetime, timedelta #timedleta 날짜 빼거나 더하는거

class NaverNewsSpider(scrapy.Spider):
    name = "naver_news" # 이름만 맞춰주면 된다.

    def start_requests(self): 
        urls = []
        # 날짜관리 (10일치만 크롤링)
        date_today = datetime.now()
        for day in range(10):
            target_day = date_today - timedelta(days=day)
            # 10일치를 2페이지씩 크롤링하겠다.
            for page in range(1,3): # 1,2
                urls.append(BASE_URL.format(target_day.strftime('%Y%m%d'),page))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #yield를 한다. self.parse는 밑에 def parse함수임.

    def parse(self, response):
        #page = response.url.split("/")[-2]
        description = response.css('.lede::text').get()
        print(description)
