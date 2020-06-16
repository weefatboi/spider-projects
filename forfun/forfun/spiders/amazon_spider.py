import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    allowed_domains = ['amazon.com']

    # no start_urls this time
    # created an argument that appends the search term to the amazon url
    # running "scrapy crawl amazon" and adding the argument "-a category=<some-search-term>"
    # will scrape the results page of that term
    def __init__(self, category=None, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.amazon.com/s?k=%s' % category]

    # access name, price, star rating and number of reviews by search-returned item
    # longer xpath specifics added to exclude hmtl results from the filter sidebar
    def parse(self, response):
        item_name = response.xpath('.//span[@data-component-type="s-search-results"]//a[@class="a-link-normal a-text-normal"]/span/text()').extract()    
        price = response.xpath('.//span[@data-component-type="s-search-results"]//span[@class="a-price"]/span/text()').extract()    
        rating = response.xpath('.//span[@data-component-type="s-search-results"]//span[@class="a-icon-alt"]/text()').extract()  
        no_reviews = response.xpath('.//span[@data-component-type="s-search-results"]//span[@class="a-size-base"]/text()').extract()  


        for item in zip(item_name, price, rating, no_reviews):
            amazon_data = {

                'item_name':item[0],
                'price':item[1],
                'rating':item[2],
                'no_reviews':item[3],

            }

            yield amazon_data  

    #### NOTES ####
    # further tweaks added to settings.py
    # set up a DOWNLOADER middleware that randomly round-robins through USER_AGENTS
    # added a list of universal agents to the USER_AGENTS setting that the DOWNLOADER can select from

    # above measures were to circumvent a HTTP 503 error from Amazon's robot detection

    # finally, CONCURRENT_REQUESTS were set to value of <1> and DOWNLOAD_DELAY to value of <3> seconds




