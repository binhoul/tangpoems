#!/usr/bin/python
#-*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from songci.items import SongciItems


class SongciSpider(Spider):
    name = "songci"
    allow_domains = ["songci.org"] #?
    start_urls = ["http://www.xigutang.com/songci300/"]
    
    def parse(self, response):

