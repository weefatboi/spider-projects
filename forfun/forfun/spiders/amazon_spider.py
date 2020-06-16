import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'

    allowed_domains = ['amazon.com']

    def __init__(self, category=None, *args, **kwargs):
        super(AmazonSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.amazon.com/s?k=%s' % category]


    def parse(self, response):
        item_name = response.xpath('.//a[@class="a-link-normal a-text-normal"]/span/text()').extract()    
        price = response.xpath('.//span[@class="a-price"]/span/text()').extract()    
        # rating = response.xpath('.//a[@class="storylink"]/text()').extract()  

        for item in zip(item_name, price):
            amazon_data = {

                'item_name':item[0],
                'price':item[1],
                # 'points':item[2],

            }

            yield amazon_data  



