# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Products(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    delivery_price = scrapy.Field()
    rating = scrapy.Field()
    no_of_review = scrapy.Field()
    delivery_price = scrapy.Field()
    seller = scrapy.Field()
    seller_rating = scrapy.Field()
    delivery_rating = scrapy.Field()
    stock = scrapy.Field()
    pass
