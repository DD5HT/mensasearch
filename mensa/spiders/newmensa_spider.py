import scrapy

class MensaSpider(scrapy.Spider):
    name = "newmensa"
    allowed_domains = ["stw-on.de"]
    start_urls = ["http://www.stw-on.de/braunschweig/essen/menus/mensa-1"]

    def parse(self, response):
        i = 1
        for table in response.xpath("//table"):
            day = table.xpath("./tr/th[@colspan='2']/text()").extract()
            print "\n"
            print day

            for tr in table.xpath(".//tr"): 
                for td in tr.xpath(".//td[@class='swbs_speiseplan_meal']/text()"):
                    meal = td.extract()
                    print meal
                    
                    for td in tr.xpath(".//td[@class='swbs_speiseplan_price_s'][1]/text()"):
                        price = td.extract()
                        print price 
