import scrapy
import json



class HomeFinderSpider(scrapy.Spider):
    name = 'homefinder'

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

        }

    def start_requests(self):
        city = 'Kent'
        state = 'OH'

        # set start url to use site's api
        start_urls = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%7B%22city%22:%22{}%22,%22state%22:%22{}%22%7D').format(city, state, city, state)

        

        yield scrapy.Request(start_urls, headers=self.headers, callback=self.parse)

    #     headers = {
    #         'Accept': 'application/json, text/plain, */*',
    #         'Accept-Encoding': 'gzip, deflate, br',
    #         'Accept-Language': 'en-US,en;q=0.9',
    #         'Cache-Control': 'no-cache',
    #         'Connection': 'keep-alive',
    #         'Host': 'api.homefinder.com',
    #         'Origin': 'https://homefinder.com',
    #         'Pragma': 'no-cache',
    #         'Referer': 'https://homefinder.com/',
    #         'Sec-Fetch-Dest': 'empty',
    #         'Sec-Fetch-Mode': 'cors',
    #         'Sec-Fetch-Site': 'same-site',
    #     }

    #     yield scrapy.Request(url, callback=self.parse, headers=headers)


    def parse(self, response):
        result = json.loads(response.body)
        print(result)

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
            
        
        
        
        
        



