from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from  mensa.items import MealEntry

class MensaSpider(CrawlSpider):
    name = 'mensa'
    allowed_domains = ['stw-on.de']
    start_urls = ['http://www.stw-on.de/speiseplane']
    rules = [Rule(LinkExtractor(allow=['http://www.stw-on.de/braunschweig/essen/menus/*']), 'parse_plan')]

    def parse_plan(self, response):
        mensa = response.url.split("/")[-1]
        tables = response.xpath(".//table[@class='swbs_speiseplan']")
        for table in tables:
            date = table.xpath(".//th[@colspan='3']/text()").extract()
            for tr in table.xpath(".//tr"):
                meal = MealEntry()
                meal["mensa"] = [mensa]
                meal["date"] = date
                meal["kind"] = tr.xpath(".//td[@class='swbs_speiseplan_kind_meal']/nobr/text()").extract()
                meal["description"] = tr.xpath("((.//td[@class='swbs_speiseplan_other'])/text())[1]").extract()
                meal["price_student"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                meal["price_employe"] = tr.xpath(".//td[@class='swbs_speiseplan_price_e']/text()").extract()
                meal["price_guest"] = tr.xpath(".//td[@class='swbs_speiseplan_price_g']/text()").extract()

                if not meal["description"]:
                    continue
                else:
                    yield meal
