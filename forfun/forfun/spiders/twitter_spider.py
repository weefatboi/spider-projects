import scrapy


class TwitterSpider(scrapy.Spider):
    name = "twitter"

    allowed_domains = ['twitter.com']

    # url encoding changes hashtag to %23 in twitter's base search url
    # double percent signs used to escape
    def __init__(self, category=None, *args, **kwargs):
        super(TwitterSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://twitter.com/search?q=%%23%s' % category]

    def parse(self, response):
        pass
    




