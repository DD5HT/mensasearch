# -*- coding: utf-8 -*-

# Scrapy settings for mensa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mensa'

SPIDER_MODULES = ['mensa.spiders']
NEWSPIDER_MODULE = 'mensa.spiders'

ITEM_PIPELINES = {
        'mensa.save_to_db.MensaPipeline': 900,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mensa (+http://www.yourdomain.com)'
