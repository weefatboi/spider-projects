import scrapy
import json
import os



class RealtorSpider(scrapy.Spider):
    name = 'realtor'

    city = 'Kent'
    state = 'OH'

    try:
        os.remove('realtor_data.json')
    except OSError:
        pass

    def start_requests(self):
        
        # set start url to use site's api
        start_urls = ('https://www.realtor.com/realestateandhomes-search/{}_{}').format(self.city, self.state)

        

        yield scrapy.Request(start_urls, callback=self.parse)

    def parse(self, response):






