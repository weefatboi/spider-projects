import scrapy


class TwitterSpider(scrapy.Spider):
    name = "twitter"

    start_urls = [

        "https://twitter.com/search?q=%23finance&src=typed_query"

    ]

    def parse(self, response):
        text_body = response.xpath('.//div[@data-testid="tweet"]//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]/text()').extract()
        username = response.xpath('.//div[@class="css-1dbjc4n r-zl2h9q"]//span[@class="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"]/text()').extract()
        
        import pdb; pdb.set_trace()
        for item in zip(text_body, username):
            finance_data = {

                'text':item[0],
                'username':item[1],

            }

            yield finance_data
    




