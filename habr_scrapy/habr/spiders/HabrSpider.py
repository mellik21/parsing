from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule

from habr_scrapy.habr.items import HabrItem


class HabrSpider(CrawlSpider):
    name = "HabrSpider"
    allowed_domains = ["habr.com/ru/"]
    start_urls = ["https://habr.com/ru/"]
    rules = (
        Rule(LinkExtractor(allow=('/page\d+/',)), callback='parse_page'),
    )

    def parse_start_url(self, response):
        return self.parse_page(response)

    def parse_page(self, response):
        root = Selector(response)
        posts = root.xpath('//article[@class="post post_preview"]')
        for post in posts:
            item = HabrItem()
            item['title'] = post.xpath('.//a[@class="post__title_link"]/text()').extract()[0]
            item['author'] = \
                post.xpath('.//span[@class="user-info__nickname user-info__nickname_small"]/text()').extract()[0]
            item['stars'] = post.xpath('.//span[@class="bookmark__counter js-favs_count"]/text()').extract()[0]
            yield item


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'FEED_URI': 'habr.csv',
    'FEED_FORMAT': 'CSV',
})

process.crawl(HabrSpider)
process.start()
