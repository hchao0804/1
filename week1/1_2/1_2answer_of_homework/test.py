from bs4 import BeautifulSoup
path = "./1_2_homework_required/index.html"
data=[]
with open(path,'r') as f:
    Soup = BeautifulSoup(f,'lxml')
    # images = Soup.find_all("img")
    # prices = Soup.find_all('h4','pull-right')
    # titles = Soup.find_all('a',href="#")
    # reviews = Soup.find_all('p','pull-right')
    # stars = Soup.find_all('span',class_='glyphicon glyphicon-star')
    titles = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')  # 复制每个元素的css selector 路径即可
    images = Soup.select('body > div > div > div.col-md-9 > div > div > div > img')
    reviews = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    prices = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    stars = Soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)')
    # print(images,prices,titles,reviews,stars,sep='\n--------\n')

for title,image,review,price,star in zip(titles,images,reviews,prices,stars):
    info = {
        'title': title.get_text(),
        'image': image.get('src'),
        'review': review.get_text(),
        "price": price.get_text(),
        'star': len(star.find_all("span",class_='glyphicon glyphicon-star'))
    }
    data.append(info)
for i in data:
    if i['star']>=4:
        print(i)