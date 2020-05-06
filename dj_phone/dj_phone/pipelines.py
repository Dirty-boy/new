# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DjPhonePipeline(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='127.0.0.1', user='root', password='123456', port=3306,db='spider', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        price = item['price']
        info = item['info']
        comment = item['comment']
        shop = item['shop']
        sql = 'insert into jd(title,price,info,comment,shop) values ("%s","%s","%s","%s","%s")' % (
            title, price, info, comment, shop)
        print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
