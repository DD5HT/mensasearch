# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MensaItem(scrapy.Item):
    day = scrapy.Field()
    kiday = scrapy.Field()
    kind = scrapy.Field()
    kind_meal = scrapy.Field()
    price = scrpay.Field()

