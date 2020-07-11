import scrapy
import json
import os



class HomeFinderSpider(scrapy.Spider):
    name = 'homefinder'

    headers = {
        
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

        }

    city = 'Kent'
    state = 'OH'

    try:
        os.remove('listing_data.json')
    except OSError:
        pass

    def start_requests(self):
        
        # set start url to use site's api
        start_urls = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%7B%22city%22:%22{}%22,%22state%22:%22{}%22%7D').format(self.city, self.state, self.city, self.state)

        

        yield scrapy.Request(start_urls, headers=self.headers, callback=self.parse)


    def parse(self, response):
        results = json.loads(response.body)
        for i in range(1, results['meta']['pages']+1):
            page = str(i)
            next_url = ('https://api.homefinder.com/v1/listing?scope=index&term={},+{}&'
                'area=%7B%22city%22:%22{}%22,%22state%22:%22{}%22%7D&page={}').format(self.city, self.state, self.city, self.state, page)
            yield response.follow(next_url, callback=self.parse_detail)


    def parse_detail(self, response):
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
                'desc':listing.get('description'),
                'nbhd':listing.get('neighborhood'),
            } 


                
        
        
        
        
        



