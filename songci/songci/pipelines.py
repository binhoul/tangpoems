# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
#from scrapy.core.exceptions import DropItem
from twisted.enterprise import adbapi
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.contrib.pipeline.images import ImagesPipeline
import time
import MySQLdb
import MySQLdb.cursors


class MySQLStorePipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
                db = 'app_redwallcofee65',
                user = 'root',
                passwd = 'fengmao',
                cursorclass = MySQLdb.cursors.DictCursor,
                charset = 'utf8',
                use_unicode = False
        )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
#        query.addErrback(self.handle_error)
        return item
  
    def _conditional_insert(self, tx, item):
            tx.execute("insert into songci (title, author, url, content) values (%s, %s, %s, %s)",
                (item['title'],  item['author'], item['url'], 
                item['content'])
            )
