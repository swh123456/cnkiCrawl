# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
sys.path.append("..")
from items import Cnki
from MysqlOperation.MysqlConnection import cnkiOper

class CnkicrawlPipeline(object):
    def process_item(self, item):

        mysql=cnkiOper()
        mysql.add(item)

        return item
# if __name__ == '__main__':
#     test=CnkicrawlPipeline()
#     item=Cnki()
#     a='你好'
#     item['title']=a
#     item['abs']="你说的但是你发布机构你的规划建 "
#     item['myStTime']=1234355
#     test.process_item(item)
#     print test.process_item(item)