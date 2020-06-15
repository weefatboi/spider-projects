import scrapy


class TwitterSpider(scrapy.Spider):
    name = "twitter"

    allowed_domains = [

        "https://twitter.com/",
        "https://mobile.twitter.com/",

    ]

    start_urls = [

        "https://twitter.com/explore"

    ]

    




