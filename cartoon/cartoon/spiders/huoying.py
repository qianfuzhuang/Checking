# -*- coding: utf-8 -*-
import scrapy
from ..items import CartoonItem


class HuoyingSpider(scrapy.Spider):
    name = 'huoying'
    allowed_domains = ['bbs.huoying666.com/']
    start_urls = ['http://bbs.huoying666.com/forum.php?mod=forumdisplay&fid=53&filter=typeid&typeid=1']

    def parse(self, response):
        item=CartoonItem()
        pages=response.xpath('//ul[@id="waterfall1"]/li')
        for page in pages:
            herf='http://bbs.huoying666.com/'+page.xpath('./div[@class="c cl"]/a/@href').get()
            title=page.xpath('./div[@class="c cl"]/a/@title').get()
            # print(herf)
            item['herf']=herf
            item['title']=title
            yield scrapy.Request(herf, callback=self.parse_pag_detail, meta=item,dont_filter=True)
    def parse_pag_detail(self,response):
        item=response.meta
        jpeg=response.xpath('//tr/td[@class="t_f"]/ignore_js_op[1]/img/@file').extract()
        # voice=response.xpath('//font[@size="5"]/a/@href').get()
        item['jpeg']=jpeg
        # item['voice']=voice
        yield item


