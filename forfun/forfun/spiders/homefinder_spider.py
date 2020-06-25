import scrapy
import json
from pprint import pprint



class HomeFinderSpider(scrapy.Spider):
    name = 'homefinder'

    allowed_domains = ['homefinder.com']

    start_urls = ['homefinder.com/for-sale/']

    def parse(self, response):
        city = 'Kent'
        state = 'OH'

        url = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%%7B%%22city%%22:%%22{}%%22,%%22state%%22:%%22{}%%22%%7D').format(city, state, state, city)


