# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ZhihufansPipeline(object):
    def __init__(self):
        self.file=open('mahuatengFans.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        fans_data=json.dumps(item,ensure_ascii=False)
        self.file.write(fans_data+'\n')
        return item
