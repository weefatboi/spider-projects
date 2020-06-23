# spider-projects
 a collection of all personal web crawler projects<br/>
 --> **UPDATE 6/17/2020:** settings.py and middlewares.py have been improved to enable ***rotating proxy*** and ***random user agent*** functionality; credit to [scrapy-rotating-proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) and [scrapy-user-agents](https://github.com/hyan15/crawler-demo/tree/master/crawling-basic/scrapy_user_agents)

# [1] Steam spider
scrapes from the [Steam Top Sellers](https://store.steampowered.com/search/?filter=topsellers) list and outputs curated deals under $10 in an email to the user<br/>
- see [prices_spider.py](spiders/prices_spider.py) for spider code<br/>
- see [scrape_send.py](other_scripts/scrape_send.py) for emailer code with [AWS SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html)<br/>

### sample email output:
<img src="images/steam-sample-output.png" width="500">


# [2] HackerNews spider
scrapes [HackerNews](https://news.ycombinator.com/) article titles, source links, and upvote points<br/>
-- see 'forfun' (projects folder) > forfun > spiders > hackernews_spider.py for spider code<br/>
-- see 'forfun' (projects folder) > news_data.json for sample json crawler output  

### sample news output:
<img src="images/hackernews-sample-output.png" width="750">


# [3] Amazon spider
scrapes [Amazon](https://www.amazon.com/) market results by search term. can provide category=< some-search-term > in cmd to scrape that item's results<br/> 
-- see 'forfun' (projects folder) > forfun > spiders > amazon_spider.py for spider code<br/>
-- see 'forfun' (projects folder) > amazon_data.json for sample json crawler output

### sample news output:
<img src="images/amazon-sample-output.png" width="750">

