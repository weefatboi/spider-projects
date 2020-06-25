import scrapy
import json
from pprint import pprint



class HomeFinderSpider(scrapy.Spider):
    name = 'homefinder'

    allowed_domains = ['homefinder.com']

    start_urls = ['https://homefinder.com/']

    # headers = {
    #     "Server":"nginx/1.13.12",
    #     "Content-Type":"application/json",
    #     "Transfer-Encoding":"chunked",
    #     "Vary":"Accept-Encoding",
    #     "X-Powered-By":"PHP/7.3.10",
    #     "Cache-Control":"no-cache, private",
    #     "Access-Control-Allow-Credentials":"true",
    #     "Content-Encoding":"gzip",
    #     }

    headers = {

        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://homefinder.com/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
        
    }

    def parse(self, response):
        city = 'Kent'
        state = 'OH'

        url = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%7B%22city%22:%22{}%22,%22state%22:%22{}%22%7D').format(city, state, city, state)

        yield scrapy.Request(url, callback=self.parse_detail, headers=self.headers)

    def parse_detail(self, response):
        result = json.loads(response.body)

        local = result['listings']['city']
        state_abrv = result['listings']['state']
        zipcode = result['listings']['zip']
        address = result['listings']['addressLine1']
        year_built = result['listings']['yearBuilt']
        bed = result['listings']['bed']
        bath = result['listings']['bath']
        ptype = result['listings']['propertyType']
        price = result['listings']['price']
        sqft = result['listings']['squareFootage']
        desc = result['listings']['description']
        nbhd = result['listings']['neighborhood']

        for item in zip(local, state_abrv, zipcode, address, year_built, bed, bath, ptype, price, sqft, desc, nbhd):
            listing_data = {
                'city':item[0],
                'state':item[1],
                'zipcode':item[2],
                'address':item[3],
                'year_built':item[4],
                'bed':item[5],
                'bath':item[6],
                'ptype':item[7],
                'price':item[8],
                'sqft':item[9],
                'desc':item[10],
                'nbhd':item[11],
            } 

            yield listing_data
            
        
        
        
        
        



