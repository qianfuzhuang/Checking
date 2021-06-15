import requests
import json, urllib
from lxml import etree

url = 'https://movie.douban.com/top250'+'?start=%d&filter='
n = 0
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}
info = []


def download_image(pictureurl):
    global n
    filename = str(n) + '.jpg'
    urllib.request.urlretrieve(url=pictureurl, filename='D:\yx\%s' % (filename))
    int(n)
    n = n + 1
    print('----图片：%s保存成功-----------' % (filename))


for i in range(1, 9):
    url1=url%(i*25)
    response = requests.get(url=url1, headers=header, timeout=5)
    print(response.status_code)
    response.encoding = 'utf-8'
    content = response.text
    html = etree.HTML(content)
    result = html.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for list in result:
        pictureurl = list.xpath('./div/div[1]/a/img/@src')[0]
        download_image(pictureurl)
        # 电影名称
        movie_name = list.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        # 主题
        item = list.xpath('./div/div[2]/div[2]/p[2]/span/text()')[0]

        # 国家
        country = list.xpath('./div/div[2]/div[2]/p[1]/text()[2]')[0]
        # 演员
        act = list.xpath('./div/div[2]/div[2]/p[1]/text()[1]')[0]
        # 评分
        score = list.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        # 保存到列表
        info.append({'电影名称': movie_name, '主题': item, '国家': country, '演员':
            act, '评分': score})
    print("第%d页保存成功" % i)
# 保存到本地json文件
with open('D:\yx\豆瓣电影.json', 'w', encoding='utf-8') as fp:
    json.dump(info, fp=fp, ensure_ascii=False, indent=5)
print('job信息保存成功')