import requests
import time
from bs4 import BeautifulSoup
import urllib.request

url = 'https://api.yii.dgtle.com/v2/index?perpage=14&page={}'


def get_page(url):
    wb_data = requests.get(url)
    json_data = wb_data.json()                        # 响应的数据格式的json类型

    for one_json in json_data['list']:
        data = {
            'img': one_json['pic'],
            'link': 'http://www.dgtle.com/article-{}-1.html'.format(one_json['aid']),      # 观察可得，文章链接由数据中的aid所拼接
            'title': one_json['title']
        }
        print(data)


def get_more_pages(start, end):
    for one in range(start, end):
        get_page(url.format(one))
        time.sleep(2)

get_more_pages(1,10)
