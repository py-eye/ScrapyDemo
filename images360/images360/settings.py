# -*- coding: utf-8 -*-

# Scrapy settings for images360 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'images360'

MAX_PAGE = 50

SPIDER_MODULES = ['images360.spiders']
NEWSPIDER_MODULE = 'images360.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'images360 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# Scrapy框架默认遵守 robots.txt 协议规则，robots规定了一个网站中，哪些地址可以请求，哪些地址不能请求。
# 默认是True，设置为False不遵守这个协议。
ROBOTSTXT_OBEY = False

# mongodb config
MONGODB_HOST = "127.0.0.1"
MONGODB_PORT = 27017
MONGODB_DBNAME = "scrapy_demo"
MONGODB_SHEETNAME = "images"

IMAGES_STORE = "E:\scrapyfiles\images360"


# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置scrapy的请求连接数，默认会同时并发16个请求
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延时，请求和请求之间的间隔，降低爬取速度，default: 0
#DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN：针对网站(主域名)设置的最大请求并发数。
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# CONCURRENT_REQUESTS_PER_IP：某一个IP的最大请求并发数。
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 是否启用Cookie的配置，默认是可以使用Cookie的。主要是针对一些网站是禁用Cookie的。
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS：配置默认的请求头Headers.
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 配置自定义爬虫中间件，scrapy也默认启用了一些爬虫中间件，可以在这个配置中关闭。
#SPIDER_MIDDLEWARES = {
#    'images360.middlewares.Images360SpiderMiddleware': 543,
#}

# 下载中间件，配置自定义的中间件或者取消Scrapy默认启用的中间件。
# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'images360.middlewares.Images360DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}


# 配置自定义的PIPELINES，或者取消PIPELINES默认启用的中间件。
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'images360.pipelines.ImagePipeline': 300,
    'images360.pipelines.MongoPipeline': 301
}


# 限速配置
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

# 是否开启自动限速
#AUTOTHROTTLE_ENABLED = True

# 配置初始url的下载延时
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5

# 配置最大请求时间
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60

# 配置请求和请求之间的下载间隔，单位是秒
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# 关于Http缓存的配置，默认是不启用。
# 对于同一个页面的请求进行数据的缓存，如果后续还有相同的请求，直接从缓存中进行获取。
# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
