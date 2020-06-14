import scrapy


class HackernewsSpider(scrapy.Spider):
    name = "hackernews"

    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        # extracting content with xpath selectors
        title = response.xpath('.//a[@class="storylink"]/text()').extract()
        source = response.xpath('.//a[@class="storylink"]/@href').extract()
        points = response.xpath('.//span[@class="score"]/text()').extract()
        
        # adding content to dict in rowS
        for item in zip(title, source, points):
            news_data = {

                'title':item[0],
                'source':item[1],
                'points':item[2],

            }

            yield news_data
            
        # join next page link to start url and scrape succeeding pages
        next_page = response.xpath('.//a[@class="morelink"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


