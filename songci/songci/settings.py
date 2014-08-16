# -*- coding: utf-8 -*-

# Scrapy settings for songci project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'songci'

SPIDER_MODULES = ['songci.spiders']
NEWSPIDER_MODULE = 'songci.spiders'
DEFAULT_ITEM_CLASS = 'songci.items.SongciItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'songci (+http://www.yourdomain.com)'
ITEM_PIPELINES = {'songci.pipelines.MySQLStorePipeline': 1}
