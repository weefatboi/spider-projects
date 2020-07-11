# spider-projects
 a collection of all personal web crawler projects<br/>
 - [settings.py](forfun/forfun/settings.py) and [middlewares.py](forfun/forfun/middlewares.py) have been improved to enable ***rotating proxy*** and ***random user agent*** functionality

# Steam spider
scrapes from the [Steam Top Sellers](https://store.steampowered.com/search/?filter=topsellers) list and outputs curated deals (under $10) in an email to the user<br/>
- see [prices_spider.py](forfun/forfun/spiders/prices_spider.py) for spider code<br/>
- see [scrape_send.py](forfun/forfun/other_scripts/scrape_send.py) for emailer code with [AWS SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)<br/>

### sample email output:
<img src="images/steam-sample-output.png" width="500">


# HackerNews spider
scrapes [HackerNews](https://news.ycombinator.com/) article titles, source links, and upvote points<br/>
- uses pagination to access subsequent articles pages
- see [hackernews_spider.py](forfun/forfun/spiders/hackernews_spider.py) for spider code<br/>
- see [news_data.json](forfun/news_data.json) for sample output in json  

### sample news output:
<img src="images/hackernews-sample-output.png" width="750">


# Amazon spider
scrapes [Amazon](https://www.amazon.com/) market results by search term.<br/>
user can provide `category= <some-search-term>` in cmd line to scrape that term's results<br/> 
- see [amazon_spider.py](forfun/forfun/spiders/amazon_spider.py) for spider code<br/>
- see [amazon_data.json](forfun/amazon_data.json) for sample output in json

### sample search results output:
<img src="images/amazon-sample-output.png" width="750">


# HomeFinder spider
scrapes [HomeFinder](https://homefinder.com/) site for real estate listing information by City and State terms<br/>
accesses website's structured json response instead of referencing html<br/>
- see [homefinder_spider.py](forfun/forfun/spiders/homefinder_spider.py) for spider code<br/>
- see [listing_data.json](forfun/listing_data.json) for sample output


# Credits
1. [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies)
2. [scrapy-user-agents](https://github.com/hyan15/crawler-demo/tree/master/crawling-basic/scrapy_user_agents)
3. [Scrapy](https://scrapy.org/)
4. [AWS SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)












