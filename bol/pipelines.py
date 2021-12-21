# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import os
import pymongo

# class BolPipeline(object):
#
#     def open_spider(self, spider):
#         self.filesExported = {}
#
#     def close_spider(self, spider):
#         pass
#
#     def exportItem(self, item):
#         productID = item['productID']
#         productName = item['productName']
#         if not os.path.exists('output'):
#             os.mkdir('output')
#         if productID not in self.filesExported:
#             f = open('output/'+productID+'.json', 'wb')
#             exporter = JsonItemExporter(f)
#             exporter.start_exporting()
#             exporter.export_item(item)
#             exporter.finish_exporting()
#             f.close()
#             self.filesExported[productID] = exporter
#             return self.filesExported[productID]
#         else:
#             return None
#
#     def process_item(self, item, spider):
#         exporter = self.exportItem(item=item)
#         return item

import logging
import pymongo
import certifi


class BolPipeline(object):

    collection_name = 'testcollection'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        self.client = pymongo.MongoClient(self.mongo_uri, tlsCAFile=certifi.where())
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        ## clean up when spider is closed
        self.client.close()

    def process_item(self, item, spider):
        ## how to handle each post
        self.db[self.collection_name].insert_one(dict(item))
        logging.debug("Post added to MongoDB")
        return item
