# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request, FormRequest
# from prospects.items import ItcItem
# from scrapy.loader import ItemLoader
# import re
# import json
# import datetime
from collections import OrderedDict
# TODO: Individual crawl delay for each spider. See if global setting overrides local spider setting.

class get_countriesSpider(scrapy.Spider):
    name = 'cities'
    start_urls = ['https://www.indeed.com/worldwide']
    # custom_settings = {
    #     'DOWNLOAD_DELAY': '3',
    # }

    countries = []

    cities_data = {}



    # is_yield_item = False

    def parse(self, response):
        # get params to create post request for all data
        self.countries = response.xpath('//table/tr[@class="countries"]/td/a/text()').extract()
        yield FormRequest('https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname:_A', callback=self.parse_list, dont_filter=True)

    def parse_list(self, response):
        tags = response.xpath('//table[@class="wikitable sortable"]/tbody/tr')
        for c in tags:
            city = c.xpath('./td[1]/a/@title').extract_first()
            country = c.xpath('./td[2]/a/@title').extract_first()
            if not city:
                continue

            item = OrderedDict()
            item['country'] = country
            item['city'] = city

            yield item

            # if not self.cities_data.get(country):
            #     self.cities_data[country] = []
            # self.cities_data[country].append(city)
            # break
        if not response.meta.get('pass'):
            urls = response.xpath('//ul/li/center/a[contains(@href,"/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/cityname")]/@href').extract()
            for url in urls:
                yield FormRequest(response.urljoin(url), callback=self.parse_list, dont_filter=True, meta={'pass': True})
