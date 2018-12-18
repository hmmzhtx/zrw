# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import ZrItem

class ZrPipeline(object):
    def __init__(self):
        self.file = open('C:\work\ming.txt', 'a')

    def process_item(self, item, spider):
        if isinstance(item, ZrItem):
            title = item['title'][0]
            print title
            self.file.write(title.encode("utf-8").strip())
            self.file.write('\n')
        return item
