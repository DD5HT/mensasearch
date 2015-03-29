from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mensa.items import MealEntry

class MealSpider(CrawlSpider):
    name = 'meal'
    allowed_domains = ['stw-on.de']
    start_urls = ['http://www.stw-on.de/speiseplane']
    rules = [Rule(LinkExtractor(allow=['essen/menus/*']), 'parse_plan')]
    pipelines = ['meal']

    def parse_plan(self, response):
        mensa = response.url.split("/")[-1]
        tables = response.xpath(".//table[@class='swbs_speiseplan']")
        for table in tables:
            date = table.xpath(".//th[@colspan='3']/text()").extract()
            trs = iter(table.xpath(".//tr"))
            trs.next()
            for tr in table.xpath(".//tr"):
                meal = MealEntry()
                meal["mensa"] = [mensa]
                meal["date"] = date
                meal["kind"] = tr.xpath(".//td[@class='swbs_speiseplan_kind_meal']/nobr/text()").extract()
                meal["description"] = tr.xpath("((.//td[@class='swbs_speiseplan_other'])/text())[1]").extract()
                meal["price_student"] = tr.xpath(".//td[@class='swbs_speiseplan_price_s']/text()").extract()
                meal["price_employee"] = tr.xpath(".//td[@class='swbs_speiseplan_price_e']/text()").extract()
                meal["price_guest"] = tr.xpath(".//td[@class='swbs_speiseplan_price_g']/text()").extract()
                tr_next = trs.next()
                if tr_next:
                    meal["food_lables"] = tr_next.xpath(".//td[@class='swbs_speiseplan_other']/nobr/img/@title").extract() # lables
                meal["allergenes"] = tr.xpath(".//img[@src='http://www.stw-on.de/media/hg-icon/A.16.png']/@title").extract() # allergenes
                meal["additives"] = tr.xpath(".//img[@src='http://www.stw-on.de/media/hg-icon/Z.16.png']/@title").extract()
                meal["special"] = tr.xpath(".//img[@src='http://www.stw-on.de/media/hg-icon/S.16.png']/@title").extract() #special
                yield meal
