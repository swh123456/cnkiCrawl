# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CnkicrawlItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class Auth(Item):
    cnki_id=Field()
    id=Field()
    title=Field()
    uniq_id=Field()
class Cnki(Item):
    cnki_id=Field()
    title=Field()
    abs=Field()
    myStTime=Field()




