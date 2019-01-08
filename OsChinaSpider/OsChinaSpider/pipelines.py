# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from .tools import DBHelper
import pymysql
import importlib,sys
importlib.reload(sys)

class OschinaspiderPipeline(object):
    def process_item(self, item, spider):
        sql = '''insert into oschina (id,project_no,name,publish_time,cycle,apply_count,view_count,budget_min_by_yuan,budget_max_by_yuan,link) 
                                SELECT {},'{}','{}','{}',{},{},{},{},{},'{}'
                                from DUAL  
                                where not exists(select id from oschina where project_no='{}');
        '''.format(item['id'],item['projectNo'],item['name'],item['publishTime'],item['cycle'],item['applyCount'],item['viewCount'],item['budgetMinByYuan'],item['budgetMaxByYuan'],'https://zb.oschina.net/project/detail.html?id={}'.format(item['id']),item['projectNo'])
        print(sql)
        dbhelper = DBHelper()
        result = dbhelper.execute(sql,None);
        return item

class DBHelper:
    # 构造函数
    def __init__(self, host='47.100.124.78', user='ghost', pwd='1qaz@WSX3edc', db='spider_db'):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(self.host, self.user,
                                        self.pwd, self.db, charset='utf8')
        except:
            # logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            # logger.error("execute failed: " + sql)
            # logger.error("params: " + params)
            self.close()
            return False
        return True

    # 用来查询表数据
    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cur.fetchall()
