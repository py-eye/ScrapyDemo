# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    name = scrapy.Field()
    # 状态
    statu = scrapy.Field()
    # 小分类
    stype = scrapy.Field()
    # 电视台
    tv = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
