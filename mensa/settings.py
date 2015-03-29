# -*- coding: utf-8 -*-

BOT_NAME = 'mensasearch'

SPIDER_MODULES = ['mensa.spiders']
NEWSPIDER_MODULE = 'mensa.spiders'

ITEM_PIPELINES = {
        'mensa.pipelines.MealPipeline': 900,
        'mensa.pipelines.LablePipeline': 1000,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mensa (+http://www.yourdomain.com)'
