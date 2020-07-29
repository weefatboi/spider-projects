import scrapy
import json
import os



class RealtorSpider(scrapy.Spider):
    name = 'realtor'

    city = 'Kent'
    state = 'OH'

    start_urls = ['https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta']

    headers = {
        
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
            'Content-Type': 'application/json; charset=utf-8',
            'Transfer-Encoding': 'chunked',
            'Connection': 'keep-alive',
            'X-Powered-By': 'Express',
            'Vary': 'Origin, Accept-Encoding',
            'ETag': 'W/"27f6a-dAtY64tytg5l6RUJvSjDUX9d4uY"',
            'Content-Encoding': 'gzip',
            'X-Cache': 'Miss from cloudfront',
            'Via': '1.1 33aa20daaac992582a9003df568480c2.cloudfront.net (CloudFront)',
            'X-Amz-Cf-Pop': 'ORD51-C2',
            'X-Amz-Cf-Id': '7XS5dcyvLv3kTmwq-MOWtpb-8LBXZZ8s1njSfiJJBZsBFvgmDjvLyQ=='

        }

    try:
        os.remove('realtor_data.json')
    except OSError:
        pass

    def start_requests(self):

        params = {
            "query": "\n\nfragment geoStatisticsFields on Geo {\n  geo_statistics {\n    housing_market {\n      median_listing_price\n    }\n  }\n}\n\nquery ConsumerSearchQuery($query: HomeSearchCriteria!, $limit: Int, $zohoQuery: ZohoCriteria!, $offset: Int, $sort: [SearchAPISort], $sort_type: SearchSortType, $geoSupportedSlug: String!, $client_data: JSON)\n{\n  zoho(query: $zohoQuery) {\n    meta_data {\n      title\n      description\n      canonical_url\n      header_1\n      deep_links {\n        ios\n        android\n      }\n    }\n  }\n  snippets(query: $zohoQuery) {\n    snippets {\n      title\n      body {\n        text\n        data_points\n      }\n    }\n  }\n  top_real_estate_markets(query: $zohoQuery) {\n    top_real_estate_markets {\n      title\n      top_markets {\n        url\n        city\n      }\n    }\n  }\n  geo(slug_id: $geoSupportedSlug) {\n    parents {\n      geo_type\n      slug_id\n      name\n    }\n    geo_statistics {\n      housing_market {\n        listing_count\n        median_listing_price\n        median_rent_price\n        median_price_per_sqft\n        median_days_on_market\n        median_sold_price\n        month_to_month {\n          active_listing_count_percent_change\n          median_days_on_market_percent_change\n          median_listing_price_percent_change\n          median_listing_price_sqft_percent_change\n        }\n      }\n    }\n    recommended_cities: recommended (query: {geo_search_type:city, limit: 20}) {\n      geos {\n        ... on City {\n          city\n          state_code\n          geo_type\n          slug_id\n        }\n        ... geoStatisticsFields\n      }\n    }\n    recommended_neighborhoods: recommended (query: {geo_search_type:neighborhood, limit: 20}) {\n      geos {\n        ... on Neighborhood {\n          neighborhood\n          city\n          state_code\n          geo_type\n          slug_id\n        }\n        ... geoStatisticsFields\n      }\n    }\n    recommended_counties: recommended (query: {geo_search_type:county, limit: 20}) {\n      geos {\n        ... on HomeCounty {\n          county\n          state_code\n          geo_type\n          slug_id\n        }\n        ... geoStatisticsFields\n      }\n    }\n    recommended_zips: recommended (query: {geo_search_type:postal_code, limit: 20}) {\n      geos {\n        ... on PostalCode {\n          postal_code\n          geo_type\n          slug_id\n        }\n        ... geoStatisticsFields\n      }\n    }\n  }\n  home_search: home_search(query: $query,\n    sort: $sort,\n    limit: $limit,\n    offset: $offset,\n    sort_type: $sort_type,\n    client_data: $client_data,\n  ){\n    count\n    total\n    results {\n      property_id\n      list_price\n      primary_photo (https: true){\n        href\n      }\n      source {\n        agents{\n          office_name\n        }\n        type\n        spec_id\n        plan_id\n      }\n      community {\n        description {\n          name\n        }\n        advertisers{\n          office{\n            hours\n            phones {\n              type\n              number\n            }\n          }\n        }\n      }\n      products {\n        brand_name\n      }\n      listing_id\n      matterport\n      virtual_tours{\n        href\n        type\n      }\n      status\n      permalink\n      price_reduced_amount\n      other_listings{rdc {\n      listing_id\n      status\n      listing_key\n      primary\n    }}\n      description{\n        beds\n        baths\n        baths_full\n        baths_half\n        baths_1qtr\n        baths_3qtr\n        garage\n        stories\n        type\n        sub_type\n        lot_sqft\n        sqft\n        year_built\n        sold_price\n        name\n      }\n      location{\n        street_view_url\n        address{\n          line\n          postal_code\n          state\n          state_code\n          city\n          coordinate {\n            lat\n            lon\n          }\n        }\n        county {\n          name\n          fips_code\n        }\n      }\n      lead_attributes {\n        show_contact_an_agent\n      }\n      open_houses{\n        start_date\n        end_date\n        description\n        time_zone\n        dst\n      }\n      flags{\n        is_coming_soon\n        is_pending\n        is_for_rent\n        is_foreclosure\n        is_contingent\n        is_new_construction\n        is_new_listing (days: 14)\n        is_price_reduced (days: 30)\n        is_plan\n        is_subdivision\n      }\n      list_date\n      last_update_date\n      photos(limit: 5, https: true){\n        href\n        tags {\n          label\n          probability\n        }\n      }\n      tags\n      branding {\n        type\n        photo\n        name\n      }\n    }\n  }\n}",
            "variables": {
                "query": {
                    "status": [
                        "for_sale",
                        "ready_to_build"
                    ],
                    "search_location": {
                        "location": "{}, {}".format(self.city, self.state)
                    },
                    "primary": 'true'
                },
                "client_data": {
                    "device_data": {
                        "device_type": "web"
                    },
                    "user_data": {
                        "last_view_timestamp": '-1'
                    }
                },
                "limit": '42',
                "offset": '0',
                "zohoQuery": {
                    "silo": "search_result_page",
                    "location": "{}, {}".format(self.city, self.state),
                    "property_status": "for_sale",
                    "filters": {}
                },
                "geoSupportedSlug": "{}_{}".format(self.city, self.state),
                "sort_type": "relevant"
            },
            "callfrom": "SRP",
            "nrQueryType": "MAIN_SRP",
            "isClient": 'true'
        }
        
        # set start url to use site's api
        # start_urls = ['https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta']

        
        yield scrapy.FormRequest('https://www.realtor.com/api/v1/hulk?client_id=rdc-x&schema=vesta', 
                method='POST', callback=self.parse, formdata=params, headers=self.headers)

    def parse(self, response):
        
        pass





