#-*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mensa.items import LableEntry

class LableSpider(CrawlSpider):
    name = 'lable'
    allowed_domains = ['stw-on.de']
    start_urls = ['http://www.stw-on.de/braunschweig/essen/wissenswertes']
    rules = [Rule(LinkExtractor(allow=['/lebensmittelkennzeichnung']), 'parse_lable')]
    pipelines = ['lable']

    def parse_lable(self, response):
        tables = response.xpath(".//table")
        for table in tables:
            for tr in table.xpath(".//tr"):
                lable = LableEntry()
                lable["lable"] = tr.xpath(".//td/strong/text()").extract()
                lable["description"] = tr.xpath(".//td/text()").extract()
                yield lable
