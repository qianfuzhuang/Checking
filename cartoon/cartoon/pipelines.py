# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# class CartoonPipeline(object):
    # def open_spider(self, spider):
    #     self.fp = open('./cartoon.txt', mode='w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     self.fp.write('%s\t%s\n' %
    #                   (item['jpeg'], item['title']))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.fp.close()
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class CartoonPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['jpeg']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('Item contains no images')
        item['image_paths'] = image_path
        return item
