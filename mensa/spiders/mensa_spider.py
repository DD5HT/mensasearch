import scrapy

class MensaSpider(scrapy.Spider):
    name = "mensa"
    allowed_domains = ["stw-on.de"]
    start_urls = ["http://www.stw-on.de/braunschweig/essen/menus/mensa-1"]

    def parse(self, response):
        #meal = response.xpath("//table[@id='*']").extract()
        for sel in response.xpath("//table"):
            for zel in sel.xpath(".//td[@class='swbs_speiseplan_meal']/text()[1]"):
                meal = zel.extract()
                print meal 
            for price in sel.xpath(".//td[@class='swbs_speiseplan_price_s']/text()"):
                price_meal = price.extract()
                print price_meal

