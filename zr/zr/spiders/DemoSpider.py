#coding:utf-8
import logging
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from zr.items import ZrItem
from scrapy.http import Request


class DemoSpider(CrawlSpider):
    name = 'DemoSpider'
    host = 'http://www.baidu.com'

    logging.getLogger("requests").setLevel(logging.WARNING)  # 将requests的日志级别设成WARNING
    logging.basicConfig(
        level=logging.DEBUG,
        format=
        '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S',
        filename='cataline.log',
        filemode='w')

    # test = True
    def start_requests(self):
        yield Request(url='http://www.baidu.com',callback=self.parse_ph_info)

    def parse_ph_info(self, response):
        phItem = ZrItem()
        selector = Selector(response)
        div = selector.xpath('//div[@class="Body"]//p/text()').extract()
        phItem['title'] = div
        print div[0]
        yield phItem
