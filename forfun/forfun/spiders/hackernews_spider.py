import scrapy
from scrapy.selector import Selector


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"

    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        news = Selector(response)
        


        for news in response.xpath('//table[@class="itemlist"]'):
            yield {

                'title': news.xpath('.//a[@class="storylink"]/text()').extract(),
                'source': news.xpath('.//a[@class="storylink"]/@href').extract(),
                'points': news.xpath('.//span[@class="score"]/text()').extract()

            }

        next_page = response.xpath('.//a[@class="morelink"]/@href').extract()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


