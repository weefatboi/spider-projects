import scrapy
import json
from pprint import pprint


class TwitterSpider(scrapy.Spider):
    name = "twitter"

    allowed_domains = ['twitter.com']

    # url encoding changes hashtag to %23 in twitter's base search url
    # double percent signs used to escape
    def __init__(self, category=None, *args, **kwargs):
        super(TwitterSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://twitter.com/search?q=%%23%s' % category]

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'referer': 'https://twitter.com/search?q=%%23finance&src=recent_search_click',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'x-csrf-token': '94b769b45691485cc215ab3c14133d0b',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
    }

    def parse(self, response):
        url = 'https://api.twitter.com/2/search?q=%%23finance'

        yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)


    def parse_api(self, response):
        raw_data = response.body

        data = json.loads(raw_data)

        details = {}

        details['text'] = data['tweets']['full_text']

        return details



    



