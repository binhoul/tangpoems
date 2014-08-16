#!/usr/bin/python
#-*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from songci.items import SongciItem
import scrapy


class SongciSpider(Spider):
    name = "spider1"
    allow_domains = ["songci.org"] #?
    start_urls = ["http://ts300.5156edu.com/sc300/"]
    
    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//table[@bgcolor="#808080"]/table/tr/td[@width="33%"]/a/@href').extract()

        for site in sites:
            yield scrapy.Request(''.join(["http://ts300.5156edu.com/sc300/",site]),callback=self.parse_dep2)

    def parse_dep2(self,response):
        sel = Selector(response)
        item = SongciItem()
        contents = response.xpath('//table[@id="table1"]/tr/td[@class="font_14"]')
        item["url"] = response.url
        item['author'] = contents.xpath('text()')[0].extract().split()[0]
        item['title'] = contents.xpath('b/text()')[0].extract()
        item['content'] = ''
        contents_text = contents.xpath('text()')
        del contents_text[0]
        for xcontent in contents_text:
            item['content'] = ''.join([item['content'],xcontent.extract(),'\r\n'])
        item['content'].strip('\r\n')
        return item

        
