# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CartoonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    herf=scrapy.Field()
    title=scrapy.Field()
    jpeg=scrapy.Field()
    image_paths=scrapy.Field()
    # voice=scrapy.Field()
