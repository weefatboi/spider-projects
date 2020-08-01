import scrapy
import json
import os



class HomesSpider(scrapy.Spider):
    name = 'homes'

    city = 'kent'
    state = 'oh'
    start = 0
    end = 17

    url = 'https://microservices.homes.com/v1/batch/?app=hdc_portal&app_platform=desktop&debug=false'

    headers = {

            "Content-Type": 'application/json',
            'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                            'eyJ1dWlkIjoiZjQ1MDZmODYtZDkyMC00NGFiLWEwMzAtN2VjMjA0Y2NlN2VlIiwibWhfaWQiOiIiLCJpYXQiOjE1OTYyNDU3NDR9.'
                            '7Oqg_g9lSXM1qcLC6o9_nDomEe-U-NMPIBw854z4d2g'

        }


    def get_params(self):

        params = [
            {
                "name": "perform_search",
                "relative_url": "/listing/v1/search/srp/",
                "retries": 3,
                "dependencies": [],
                "method": "POST",
                "body": {
                    "start": self.start,
                    "end": self.end,
                    "sort_field": "score",
                    "sort_order": "asc",
                    "filter": {
                        "city": {
                            "value": self.city,
                            "operator": "must"
                        },
                        "region": {
                            "value": self.state,
                            "operator": "must"
                        },
                        "listing_status": {
                            "value": "for sale",
                            "operator": "must"
                        }
                    }
                }
            }
        ]

        return json.dumps(params)


    def increment_offset(self):
        yield scrapy.Request(self.url, 
                method='POST', callback=self.parse, body=self.get_params(), headers=self.headers)

        self.start = self.end + 1
        self.end += 17


    # try:
    #     os.remove('C:/Users/Owner/GitHub/spider-projects/forfun/realtor_data.json')
    # except OSError:
    #     pass


    def start_requests(self):
        return self.increment_offset()


    def parse(self, response):
        results = json.loads(response.body)
        import pdb; pdb.set_trace()
        
        for listing in results.get('results')[0].get('body').get('items'):

            yield {
                'city':listing['location']['address']['city'],
                'state':listing['location']['address']['state_code'],
                'zipcode':listing['location']['address']['postal_code'],
                'address':listing['location']['address']['line'],
                'year_built':listing['description']['year_built'],
                'bed':listing['description']['beds'],
                'bath':listing['description']['baths'],
                'ptype':listing['description']['type'],
                'price':listing['list_price'],
                'sqft':listing['description']['sqft'],
                'tags':listing.get('tags'),
            }
        
        
        if results.get('results')[0].get('body').get('total_items') > self.end:
            yield scrapy.Request(self.url, 
                method='POST', callback=self.parse, body=self.get_params(), headers=self.headers)

            self.start = self.end + 1
            self.end += 17
    




