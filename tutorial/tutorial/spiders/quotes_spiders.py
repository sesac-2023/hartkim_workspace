from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "testspider" # 이름만 맞춰주면 된다.

    def start_requests(self): # 크롤링 하고자 하는 url넣기
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/", # def안에 말고 클래스 안에 urls 넣으면 어떻게 가져오죠? self안에 있는 url 가져온다. 똑같이 동작함
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #yield를 한다. self.parse는 밑에 def parse함수임.

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

        quotes = response.css('.quote .text::attr(itemprop)').getall() # ('.quote .text::text') quote 안에 text 속성의 text를 뽑아내자
        # getall은 검색되는 모든 태그 리스트에 담고 get은 가장빨리 탐색되는 것 하나를 담는다.

        # ::text --> text속성 가져옴
        # ::attr(속성명) -> 특정 속성값 가져옴
        #print(quotes[0].attrib['itemtype'])
        print(quotes[0])

        # 파일 저장하는것, itmes 써도 괜찮다.
        datas = [' '.join(quotes), '123','456', response.url]
        with open('./result.csv','a',encoding='utf-8')as f:
            f.write(','.join(datas)+'\n')