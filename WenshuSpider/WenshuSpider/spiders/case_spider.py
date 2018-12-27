# -*- coding: utf-8 -*-
import scrapy
import traceback
import pyv8
#爬取中国裁判文书网的信息
#http://wenshu.court.gov.cn/

class CaseSpiderSpider(scrapy.Spider):
    name = 'WenShu'
    allowed_domains = ['wenshu.court.gov.cn']
    areas = [ '北京','上海','江苏','浙江','广东'] #城市
    case_type = ['刑事案件','民事案件'] #案件类型
    pageIndex = 1 #分页Index
    pageSize = 50 #单页显示数量
    start_urls = ['http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++案件类型:刑事案件']
    def start_requests(self):
        yield scrapy.request();
    def parse(self, response):
        print(response);
        try:
            for case in response.css('div.dataItem'):
                title = case.xpath('@title').extract_first();
                print("title:"+title);
                yield {
                    'title': title
                }
        except:
            traceback.print_exc()

