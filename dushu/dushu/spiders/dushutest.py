# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DushuItem

class DushutestSpider(CrawlSpider):
    name = 'dushutest'
    allowed_domains = ['dushu.com']
    start_urls = ['https://www.dushu.com']

    rules = (
        #<a href="/book/1617_1.html">1</a>
        Rule(LinkExtractor(allow=r'/book/[\d]+_[\d]+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/book/[\d]+.html'), callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        # item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        item = DushuItem()
        books=response.xpath('//div[@class="bookslist"]/ul/li')
        for book in books:
            book_name=book.xpath('.//h3/a/@title').extract()[0]
            book_url = book.xpath('.//img/@src').get()
            book_author = book.xpath('.//p[1]/text()').get()
            book_info = book.xpath('.//p[2]/text()').extract()[0]

            item['book_url'] = book_url
            item['book_name'] = book_name
            item['book_author'] = book_author
            item['book_info'] = book_info
            yield item


