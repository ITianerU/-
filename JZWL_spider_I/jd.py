import requests
from lxml import etree
import csv

start_url = "https://search.jd.com/Search?keyword=%E7%89%9B%E5%A5%B6&enc=utf-8&pvid=6d6528785b404d7fb6b499c3e6df5509"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "referer": "https://search.jd.com/Search?keyword=%E7%89%9B%E5%A5%B6&enc=utf-8&pvid=afcb19ae854144b6a21885b0c5c9a094",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

def spider(url, headers):
    rsp = requests.get(url, headers=headers)
    html = etree.HTML(rsp.content)
    items = html.xpath('//*[@id="J_goodsList"]/ul/li/div')
    l = list()
    for i in items:
        price = i.xpath('./div[3]/strong/i/text()')
        if len(price) == 0:
            price = " "
        else:
            price = price[0]
        type = i.xpath('./div[4]/a/em/span/text()')
        if len(type) == 0:
            type = "京东精选"
        else:
            type = type[0]
        titles = i.xpath('./div[4]/a/em/text() | .//div[4]/a/em/font/text() | ./div[4]/a/i/text()')
        if len(titles) == 0:
            titles = " "
        else:
            titles = ",".join(titles)
        shop = i.xpath('./div[7]//a/text()')
        if len(shop) == 0:
            shop = " "
        else:
            shop = shop[0]
        l.append([price, type, titles, shop])

    with open("data.csv", 'w') as f:
        c = csv.writer(f, delimiter=' ')
        c.writerow(['价格', '类型', '标题', '商店'])
        c.writerows(l)



if __name__ == '__main__':
    spider(start_url, headers)