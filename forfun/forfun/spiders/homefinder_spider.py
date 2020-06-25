import scrapy
import json
from pprint import pprint



class HomeFinderSpider(scrapy.Spider):
    name = 'homefinder'

    allowed_domains = ['homefinder.com']

    start_urls = ['https://homefinder.com/for-sale/']

    headers = {

        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://homefinder.com/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        
    }

    def parse(self, response):
        city = 'Kent'
        state = 'OH'

        url = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%%7B%%22city%%22:%%22{}%%22,%%22state%%22:%%22{}%%22%%7D').format(city, state, state, city)

        yield scrapy.Request(url, callback=self.parse_detail, headers=self.headers)

    def parse_detail(self, response):
        result = json.loads(response.body)

        detail = {}

        detail['city'] = result['listings']['city']
        detail['state'] = result['listings']['state']
        detail['zip'] = result['listings']['zip']
        detail['address'] = result['listings']['addressLine1']
        detail['year_built'] = result['listings']['yearBuilt']
        detail['bed'] = result['listings']['bed']
        detail['bath'] = result['listings']['bath']
        detail['type'] = result['listings']['propertyType']
        detail['price'] = result['listings']['price']
        detail['sqft'] = result['listings']['squareFootage']
        detail['desc'] = result['listings']['description']
        detail['nbhd'] = result['listings']['neighborhood']

        return detail
        
        
        
        



