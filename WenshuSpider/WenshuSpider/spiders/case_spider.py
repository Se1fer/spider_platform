# -*- coding: utf-8 -*-
import scrapy


class CaseSpiderSpider(scrapy.Spider):
    name = 'case_spider'
    allowed_domains = ['wenshu.court.gov.cn']
    start_urls = ['http://wenshu.court.gov.cn/']

    def start_requests(self):


        pass

    def parse(self, response):
        pass
