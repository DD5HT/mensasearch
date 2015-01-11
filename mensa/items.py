#
#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Hauptgericht(scrapy.Item):
    day = scrapy.Field()
    meal = scrapy.Field()
    price_s = scrapy.Field()
    price_e = scrapy.Field()
    price_g = scrapy.Field()

class Beilage(scrapy.Item):
    day = scrapy.Field()
    other  = scrapy.Field()
    price_s = scrapy.Field()
    price_e = scrapy.Field()
    price_g = scrapy.Field()
