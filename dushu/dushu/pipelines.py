# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DushuPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', port=3306,
                               user='qfz', password='12345678as',
                               database='test1', charset='utf8')
        print(self.conn)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert = 'insert into book(book_url,book_name,book_author,book_info) ' \
                 'values("%s","%s","%s","%s")'%(item['book_url'],item['book_name'],item['book_author'],item['book_info'])
        self.cursor.execute(insert)

        self.conn.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
# class DushuPipeline1:
#
#     def open_spider(self, spider):
#         self.conn = pymysql.Connect(host='localhost', port=3306,
#                                user='qfz', password='12345678as',
#                                database='test1', charset='utf8')
#         print(self.conn)
#         self.cursor = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         insert = 'insert into book(book_url,book_name,book_author,book_info) ' \
#                  'values("%s","%s","%s","%s")'%(item['book_url'],item['book_name'],item['book_author'],item['book_info'])
#         self.cursor.execute(insert)
#
#         self.conn.commit()
#         return item
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()