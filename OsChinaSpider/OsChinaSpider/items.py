# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OschinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field() #主键
    projectNo = scrapy.Field() #项目编号
    name = scrapy.Field() #项目名称
    publishTime = scrapy.Field() #发布时间
    cycle = scrapy.Field() #开发周期
    applyCount = scrapy.Field() #招标人数
    viewCount = scrapy.Field() #浏览人数
    budgetMinByYuan =  scrapy.Field() #最小金额
    budgetMaxByYuan = scrapy.Field()  # 最大金额
    skillList = scrapy.Field() #技能列表
    tagList = scrapy.Field() #标签列表
    pass
