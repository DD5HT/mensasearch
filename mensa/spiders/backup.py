import scrapy

class MensaSpider(scrapy.Spider):
    name = "mensa"
    allowed_domains = ["stw-on.de"]
    start_urls = ["http://www.stw-on.de/braunschweig/essen/menus/mensa-1"]

    def parse(self, response):
        #meal = response.xpath("//table[@id='swbs_speiseplan_mo']").extract()
        for sel in response.xpath("//table[@id='swbs_speiseplan_mo']//td[@class='swbs_speiseplan_meal']/text()"):
            meal = sel.extract()
            print meal 

       


