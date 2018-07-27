import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_links_from():                             # 无商家和个人之分，此处删除who_sells参数
    urls = []
    list_view = 'http://bj.58.com/pbdn/'          # 无需格式化字符串
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('td.t a.t'):
        url = link.get('href')                    # 不对链接进行处理，否则影响类目的抓取
        if 'zhuanzhuan' in url:                   # 此处过滤无用链接
            urls.append(url)
    return urls


# 此时浏览量已经不需要通过ajax请求得到，而在原页面即可抓取到，此处移除get_views_from方法

def get_item_info():
    urls = get_links_from()
    for url in urls:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        data = {
            'title': soup.title.text.strip(),        # 添加strip()方法，去点首尾多余的空格或者换行
            'price': soup.select('span.price_now > i')[0].text,
            'area': soup.select('div.palce_li > span > i')[0].text.split('-') if soup.select('div.palce_li > span > i') else None,
            'views': soup.select('span.look_time')[0].text,
            'cate': soup.select('span.crb_i > a')[-1].text.strip(),
            'date': str(datetime.now().strftime('%Y.%m.%d')),

        }                                            # 页面未包含日期相关的信息，所以将date设置为爬取时间，方便统计一天的交易量
        print(data)

get_item_info()