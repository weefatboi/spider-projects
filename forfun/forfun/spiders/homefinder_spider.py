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


    def parse(self, response):
        result = json.loads(response.body)

        for listing in result['listings']:

            yield {
                'city':listing['city'],
                'state':listing['state'],
                'zipcode':listing['zip'],
                'address':listing['addressLine1'],
                'year_built':listing['yearBuilt'],
                'bed':listing['bed'],
                'bath':listing['bath'],
                'ptype':listing['propertyType'],
                'price':listing['price'],
                'sqft':listing['squareFootage'],
                'desc':listing['description'],
                'nbhd':listing.get('neighborhood'),
            } 


                
        
        
        
        
        



