import scrapy
from scrapy.crawler import CrawlerProcess
from forfun.spiders.prices_spider import PricesSpider
import os
import json
import boto3
from botocore.exceptions import ClientError

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_FORMAT': 'json',
    'FEED_URI': 'steam.json'
})

process.crawl(PricesSpider)
process.start()



# spider is complete, steam.json has data
# open steam.json with python

path = 'C:/Users/Owner/GitHub/steamscraper/steam-scraper/steamscrape/steam.json'

with open(path, 'r') as f:
    data = json.load(f)

    MAX_PRICE = 10

    def email_body(i):
        return "<a href={}>{}</a> | {} | {} off!".format(i['link'], i['game'], i['price'], i['discount'])

    def price_compare(i):
        dirty = i['price'][1:]
        clean = dirty.replace(',', '')
        price = float(clean)
        return price <= MAX_PRICE
        
    email_list = [
        email_body(i)
        for i in data
        if price_compare(i)
    ]

    final_list = "<br>".join(email_list)    

    for product in data:
      product['price'] = product['price'].replace("$", "")
      product['price'] = float(product['price'])

    deals = [sub['price'] for sub in data if sub['price'] <= 10]
    msg = "There are {0} Top Sellers under TEN BUCKS!".format(len(deals))
  

# AWS SES send email with curated steams deals under 10 dollars

SENDER = "Gordon <gordonwall9@gmail.com>"

RECIPIENT = "gordonwall9@gmail.com"

AWS_REGION = "us-east-1"

SUBJECT = "Check out Today's Steam Deals..."

BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
            )
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>{msg}</h1>
  <p>{final_list}</p>
  <p>See more deals here:
    <a href='https://store.steampowered.com/specials#tab=TopSellers'>Steam</a> 
    | This email scraped using
    <a href='https://scrapy.org/'>
      Scrapy for Python</a>.</p>
</body>
</html>
            """.format(msg=msg, final_list=final_list)           

CHARSET = "UTF-8"

client = boto3.client('ses',region_name=AWS_REGION)

try:
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
	
except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])


os.remove(path)





