import scrapy
from scrapy.mail import MailSender

class PricesSpider(scrapy.Spider):
    name = "prices"
    allowed_domains = [
        'store.steampowered.com'
    ]
    start_urls = [
        'https://store.steampowered.com/specials#tab=TopSellers'
    ]

    def parse(self, response):
        for post in response.css('div#tab_content_TopSellers a.tab_item'):
            yield {
                'link': post.css('::attr(href)').get(),
                'game': post.css('.tab_item_name::text').get(),
                'discount': post.css('.discount_pct::text').get(),
                'price': post.css('.discount_final_price::text').get()
            }

        # next_page = response.css('a.btnv6_white_transparent.btn_small_tall::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

    


