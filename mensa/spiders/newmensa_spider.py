import scrapy
from mensa.items import MensaItem
class MensaSpider(scrapy.Spider):
    name = "newmensa"
    allowed_domains = ["stw-on.de"]
    start_urls = ["http://www.stw-on.de/braunschweig/essen/menus/mensa-1"]

    def parse(self, response):
        for table in response.xpath("//table"):
            item = MensaItem()
            item["day"] = table.xpath("./tr/th[@colspan='2']/text()").extract()

            for tr in table.xpath(".//tr"): 
                
                for td in tr.xpath(".//td[@class='swbs_speiseplan_meal']/text()"):
                    item["meal"] = td.extract()
                    item["price"]=tr.xpath(".//td[@class='swbs_speiseplan_price_s'][1]/text()").extract()
                    yield item
