import requests
from bs4 import  BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250'

def download_page(url):
    page = requests.get(url).content
    return page
def parse_html(html):
    info_list = []
    soup = BeautifulSoup(html,'lxml')
    images = soup.select("#content > div > div.article > ol > li > div > div.pic > a > img")
    titles = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a > span:nth-of-type(1)')
    hrefs = soup.select('#content > div > div.article > ol > li > div > div.info > div.hd > a')
    descs = soup.select('#content > div > div.article > ol > li > div > div.info > div.bd > p')
    rates = soup.find_all('span',attrs={'class':"rating_num"})
    #print(images,titles,hrefs,descs,rates,sep="\n--------------------------\n")
    for image,title,href,desc,rate in zip(images,titles,hrefs,descs,rates):
        info={
            'image': image.get('src'),
            'title': title.get_text(),
            'href': href.get('href'),
            'desc': desc.get_text(),
            'rate': rate.get_text(),
        }
        info_list.append(info)
    return info_list

def main():
    data = parse_html(download_page(DOWNLOAD_URL))
    movie_list= []
    for i in data:
        if (float)(i['rate']) > 9.3:
            movie_info = {'title':i['title'],'rate':i['rate'],'href':i['href']}
        else:
            continue
        movie_list.append(movie_info)
    print(movie_list)
if __name__ =='__main__':
    main()

