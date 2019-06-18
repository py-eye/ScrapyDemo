# -*- coding: utf-8 -*-
import scrapy
from movie.items import MovieItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        movies = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for each_movie in movies:
            item = MovieItem()
            item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
            item['statu'] = each_movie.xpath('./span[1]/font/text()').extract()[0]
            item['stype'] = each_movie.xpath('./span[@class="mjjq"]/text()').extract()[0]
            item['tv'] = each_movie.xpath('./span[@class="mjtv"]/text()').extract()[0]
            if len(each_movie.xpath('./div[2]/font/text()')):
                item['update_time'] = \
                each_movie.xpath('./div[2]/font/text()').extract()[0]
            else:
                item['update_time'] = \
                each_movie.xpath('./div[2]/text()').extract()[0]

            yield item

