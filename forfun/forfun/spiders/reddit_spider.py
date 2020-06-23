import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'

    allowed_domains = ['reddit.com']

    def __init__(self, category=None, *args, **kwargs):
        super(RedditSpider, self)
        self.start_urls = ['https://www.reddit.com/search/?q=%s' % category]

    
