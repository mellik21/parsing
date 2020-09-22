import scrapy

class HabrItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    stars = scrapy.Field()
