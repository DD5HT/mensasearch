import scrapy
from  mensa.items import Hauptgericht, Beilage 
class MensaSpider(scrapy.Spider):
    name = "mensa"
    allowed_domains = ["stw-on.de"]
    start_urls = ["http://www.stw-on.de/braunschweig/essen/menus/mensa-1",
                  "http://www.stw-on.de/braunschweig/essen/menus/360-2",
                  "http://www.stw-on.de/braunschweig/essen/menus/mensa-2",
                  "http://www.stw-on.de/braunschweig/essen/menus/mensa-hbk"]

    def parse(self, response):
        for table in response.xpath("//table"):
            haupt = Hauptgericht()
            beil = Beilage()
            haupt ["day"] = table.xpath("./tr/th[@colspan='2']/text()").extract()
            beil ["day"] = haupt["day"]
            for tr in table.xpath(".//tr"): 
                
                for td in tr.xpath(".//td[@class='swbs_speiseplan_meal']/text()"):
                    haupt["meal"]  = td.extract()
                    
                    haupt["kind_meal"] = tr.xpath(".//td/nobr/text()").extract()

                    haupt["price_s"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    
                    haupt["price_g"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    
                    haupt["price_e"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    yield haupt
                
                for td in tr.xpath(".//td[@class='swbs_speiseplan_other']/text()"):
                    beil["other"] = td.extract()
                    
                    beil["kind"] = tr.xpath(".//td/nobr/text()").extract()

                    beil["price_s"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    
                    beil["price_g"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    
                    beil["price_e"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                    yield beil 
