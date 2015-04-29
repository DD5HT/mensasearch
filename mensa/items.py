#
#-*- coding: utf-8 -*-

import scrapy

class MealEntry(scrapy.Item):
    mensa = scrapy.Field()
    kind = scrapy.Field()
    description = scrapy.Field()
    price_student = scrapy.Field()
    price_employee = scrapy.Field()
    price_guest = scrapy.Field()
    food_lables = scrapy.Field()
    allergenes = scrapy.Field()
    additives = scrapy.Field()
    special = scrapy.Field()
    date = scrapy.Field()

class LableEntry(scrapy.Item):
    lable = scrapy.Field()
    description = scrapy.Field()
