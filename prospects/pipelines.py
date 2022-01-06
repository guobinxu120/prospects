# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy import signals
# from prospects.exporters import MyCsvItemExporter
# import re
# import csv
# from collections import OrderedDict
# from prospects.items import ItcItem
# from sqlalchemy.orm import sessionmaker
# from .models import DB_Data, DB_Data_Entries, db_connect, create_tables


class DatabaseExportPipeline(object):
    cur = None
    con = None
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        pass

        # import pymysql
        #
        # self.con = pymysql.connect('localhost', 'root', '', 'scrapy')
        #
        # with self.con:
        #
        #     self.cur = self.con.cursor()
        #     self.cur.execute("SELECT VERSION()")
        #
        #     version = self.cur.fetchone()
        #
        #     print("Database version: {}".format(version[0]))

            # sql = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'indeed_data'"
            # cur.execute(sql)
            # result = cur.fetchone()
            # number_of_rows = result[0]
            # if number_of_rows == 0:



        # engine = db_connect()
        # create_tables(engine)
        # self.Session = sessionmaker(bind=engine)

    def close_spider(self, spider):
        pass

        
        # session = self.Session()
        # session.close()

    def process_item(self, item, spider):
        """

        This method is called for every item pipeline component.

        """
        # sql = "SELECT COUNT(*) FROM indeed_data WHERE job_id = '{}'".format(item.get('job id'))
        # self.cur.execute(sql)
        # result = self.cur.fetchone()
        # number_of_rows = result[0]
        # insert_sql = "INSERT INTO indeed_data(job_id, title, country, location, company, review_count, review_rating, part_time_or_full_time_or_casual, salary_or_hourly_rate, how_long_job_has_been_live, job_description, scrape_timestamp, url) " \
        #                 " VALUES ('" + item.get('job id') + "', '" + item.get('title') + "', '" + item.get('country') + "', '" + item.get('location') + "', '" + item.get('company') + "'" \
        #                 ", '" + str(item.get('review_count')) + "', '" + str(item.get('review_rating')) + "', '" + item.get('part time/full time/casual') + "', '" + item.get('salary/hourly rate') + "','" + item.get('how long job has been live') + "'" \
        #                 ", '" + item.get('job description') + "', '" + str(item.get('scrape timestamp')) + "', '" + item.get('url') + "');"
        # if number_of_rows == 0:
        #     # print(insert_sql)
        #     self.cur.execute(insert_sql)
        #     self.con.commit()
        # else:
        #     print('same job id: ' + item.get('job id'))
        #     print(insert_sql)
        #     pass
        # pass
        return item
