# -*- coding: utf-8 -*-
import scrapy


class DescoverySpider(scrapy.Spider):
    name = 'descovery'
    allowed_domains = ['xinpianchang.com']
    start_urls = ['http://xinpianchang.com/']

    def parse(self, response):
        pass
