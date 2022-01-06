# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst
import re


def clear_phone(value):
    
    if value is None:
        value = ""
    else:
        value = value.replace(" ", "")
        value = re.sub(r'^0+', "", value)
        if '+44' not in value:
            value = "+44" + value
        
    return value
    
def clear(value):

    if value is None:
        value = ""

    if isinstance(value, bytes):
        value = value.strip()

    if isinstance(value, str):
        value = value.strip()

    return value


class ItcItem(scrapy.Item):

    last_name = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    lawful_basis_source_detail_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    twitter_user_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    date_reviewed = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    account_name = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    title = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    address = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    website_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    email = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    description = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    phone_work = scrapy.Field(
        input_processor=MapCompose(clear, clear_phone),
        output_processor=TakeFirst())
    phone_mobile = scrapy.Field(
        input_processor=MapCompose(clear, clear_phone),
        output_processor=TakeFirst())
    business_pillar_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    
    target_data_source_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    lawful_basis_source = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    lawful_basis = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    account_industry_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    account_type_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    company_category_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    company_incorporation_date_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    company_sic_code1_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    
    company_status_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    companies_house_url_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    company_number_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    accounting_reference_date_c = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    pass

class EntriesItem(scrapy.Item):

    address = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    business_category = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    city = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    company_name = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    country = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    country2 = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    country3 = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    email = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    email2 = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    email4 = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    email5 = scrapy.Field(
        input_processor=MapCompose(clear, clear_phone),
        output_processor=TakeFirst())
    email6 = scrapy.Field(
        input_processor=MapCompose(clear, clear_phone),
        output_processor=TakeFirst())
    fax = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    number_of_employees_from = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    number_of_employees_to = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    phone = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    position = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    postcode = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    premises_type = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    url_match = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())
    url_match_date = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    website = scrapy.Field(
        input_processor=MapCompose(clear),
        output_processor=TakeFirst())

    pass
