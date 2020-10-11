from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from twitter_scrapy.twitter.items import Tweet
from twitter_scrapy.twitter.items import User


class TwitterSpider(CrawlSpider):
    name = "TwitterSpider"
    allowed_domains = ["https://twitter.com/Krua_nyan/"]

    # rules = (
    #     Rule(LinkExtractor(allow=('/page\d+/',)), callback='parse_page'),
    # )

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        root = Selector(response)
        tweets = root.xpath('//article[@class="post post_preview"]')
        for tweet in tweets:
            item = Tweet()
            item['text'] = tweet.xpath('.//a[@class="post__title_link"]/text()').extract()[0]
            item['author'] = \
                tweet.xpath('.//span[@class="user-info__nickname user-info__nickname_small"]/text()').extract()[0]
            item['likes'] = tweet.xpath('.//span[@class="bookmark__counter js-favs_count"]/text()').extract()[0]
            yield item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_URI': 'tweets.csv',
    'FEED_FORMAT': 'CSV',
})

process.crawl(TwitterSpider)
process.start()
