import scrapy


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"

    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        for news in response.xpath('//table[@class="itemlist"]'):
            yield {
                'title': news.xpath('.//a[@class="storylink"]/text()').getall(),
                'source': news.xpath('.//a[@class="storylink"]/@href').getall(),
                'points': news.xpath('.//span[@class="score"]/text()').getall()
            }

        next_page = response.xpath('.//a[@class="morelink"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


