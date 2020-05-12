# -*- coding: utf-8 -*-
# scrapy 是一个基于异步+多线程的方式运行爬虫的框架，内部的函数都是以回调的形式执行的，不能手动调用
from scrapy import Spider, Request
from urllib.parse import urlencode
import json
from images360.items import Images360Item


# 创建一个Spider
class ImagesSpider(Spider):
    # name 自定义的爬虫名称，运行爬虫的时候就通过这个name的值运行的。name的值是唯一的
    name = 'images'

    # allowed_domains：允许访问的网站的域名。没有设置的无法访问
    allowed_domains = ['images.so.com']

    # start_urls：指定爬虫的起始url，
    # 爬虫启动之后，Engine就会从start_urls提取第一个url，然后将url构造成一个Request对象，交给调度器
    start_urls = ['http://images.so.com/']

    # parse()函数是在start_urls中的url请求成功以后，自动回调parse()函数
    def parse(self, response):
        # 解析response对象
        result = json.loads(response.text)
        for image in result.get('list'):
            item = Images360Item()
            item['id'] = image.get('id')
            item['url'] = image.get('qhimg_url')
            item['title'] = image.get('title')
            item['thumb'] = image.get('qhimg_thumb')
            yield item

    def start_requests(self):
        data = {'ch':'beauty', 'listtype':'new'}
        base_url = "http://image.so.com/zjl?"

        for page in range(1, self.settings.get('MAX_PAGE')+1):
            data['sn'] = page * 30
            params = urlencode(data)
            url = base_url + params

            # 获取下一页的连接，然后构造一个请求对象，将这个request对象yield到调度器的队列中
            yield Request(url, self.parse)

