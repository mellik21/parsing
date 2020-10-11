import scrapy


class Tweet(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    likes = scrapy.Field()
    #  comments = scrapy.Field()
    #  reposts = scrapy.Field()
    #  date = scrapy.Field()
    pass


class User(scrapy.Item):
    name = scrapy.Field()
    nickname = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    #  tweetsNumber = scrapy.Field()
    pass
