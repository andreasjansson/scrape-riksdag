# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Member(scrapy.Item):
    namn = scrapy.Field()
    valkrets = scrapy.Field()
    epost = scrapy.Field()
    parti = scrapy.Field()
    titel = scrapy.Field()
    fodelsear = scrapy.Field()
    telefon = scrapy.Field()
    plats = scrapy.Field()
