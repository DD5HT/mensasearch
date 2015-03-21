#
#-*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MealEntry(scrapy.Item):
    mensa = scrapy.Field()
    kind = scrapy.Field()
    description = scrapy.Field()
    price_student = scrapy.Field()
    price_employe = scrapy.Field()
    price_guest = scrapy.Field()
    food_lables = scrapy.Field()
    date = scrapy.Field()
