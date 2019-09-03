# -*- coding: utf-8 -*-
import scrapy
import json

class Zhihu1Spider(scrapy.Spider):
    name = 'zhihu1'
    allowed_domains = ['zhihu.com']
    start_urls = [f'https://www.zhihu.com/api/v4/members/ponyma/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&{offset}=20&limit=20'for offset in range(0,40,20)]

    def parse(self, response):
        json_data=json.loads(response.text)
        if json_data.get('data',False):
            #粉丝信息
            for data in json_data['data']:
                #粉丝id以及粉丝是否有粉丝
                if data.get('url_token',False) and data.get('follower_count',False):
                    if data['follower_count'] < 1 :
                        break
                    #通过粉丝数计算页数
                    page= data['follower_count']//20
                    more_one_page = data['follower_count'] % 20
                    if more_one_page>0 :
                        page += 1
                    for offset in range(0,page*20,20):
                        new_url=f'https://www.zhihu.com/api/v4/members/{data["url_token"]}/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&{offset}=0&limit=20'
                        yield scrapy.Request(new_url,callback=self.parse)
                yield data

