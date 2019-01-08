# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import OschinaspiderItem
import time


class OschinaSpider(scrapy.Spider):
    name = 'OsChina'
    allowed_domains = ['zb.oschina.net']
    start_urls = ['https://zb.oschina.net/project/contractor-browse-project-and-reward?applicationAreas=&sortBy=30&currentTime=&pageSize=50&currentPage=1'];

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url);
        pass

    def parse(self, response):
        job_list = json.loads(response.body)['data']['data'];
        for job in job_list:
            oschina = OschinaspiderItem()
            oschina['id'] = job["id"];
            oschina['projectNo'] = job['projectNo'];
            oschina['name'] = job['name'];
            oschina['publishTime'] = job['publishTime'];
            oschina['cycle'] = job['cycle'];
            oschina['applyCount'] = job['applyCount'];
            oschina['viewCount'] = job['viewCount'];
            oschina['budgetMinByYuan'] = job['budgetMinByYuan'];
            oschina['budgetMaxByYuan'] = job['budgetMaxByYuan'];
            oschina['skillList'] = job['skillList'];
            oschina['tagList'] = job['tagList'];
            yield oschina
        pass
