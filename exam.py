
import requests
import json,urllib
from lxml import etree
# 首页网址（河南工学院招聘信息网）
# url = 'http://hngxy.goworkla.cn/module/campustalk/nid-5612'
# 分页爬取网址结构
url='http://hngxy.goworkla.cn/module/campustalk/nid-5612/'+'page-%d'
#获取headers
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'hngxy.goworkla.cn',
    'Referer': 'http://hngxy.goworkla.cn/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
# 定义空列表
info=[]

if __name__ == '__main__':
    n = 0
    #分页循环爬取
    for i in range(1,9):
            url_page = url%(i)
            print(url_page)
            #超时时间5秒
            response = requests.get(url=url_page, headers=headers,timeout=5)
            #获取状态码
            print(response.status_code)
            response.encoding = 'utf-8'
            content = response.text
            # 保存网页到本地
            with open('./html.html', 'w',encoding='utf-8') as fp:
                fp.write(content)
            html = etree.HTML(content)
            # 获取单个项目详细信息
            result = html.xpath('//div[@class="talk campustalk inner-content"]/a')
            print("----",result)

            for list in result:
                # 获取图片网址
                pictureurl = list.xpath('./div[@class="infoTips"]/div[@class="left"]/img/@src')[0]
                # 下载图片
                def download_image(pictureurl):
                    global n
                    filename = str(n)+'.jpg'
                    urllib.request.urlretrieve(url=pictureurl, filename='./%s' % (filename))
                    int(n)
                    n=n+1
                    print('----图片：%s保存成功-----------' % (filename))
                download_image(pictureurl)
                # 获取活动主题
                item=list.xpath('./div[@class="infoTips"]/div/p[1]/text()')[0]
                # 获取活动地址
                adress=list.xpath('./div[@class="infoTips"]/div/p[2]/text()')[0]
                # 获取活动时间
                time=list.xpath('./div[@class="infoTips"]/div/p[3]/text()')[0]
                # 获取浏览量
                num=list.xpath('./div[@class="infoTips"]/div/p[4]/text()')[0]
                #保存到列表
                info.append({'主题': item, '图片': pictureurl, '举办地点': adress, '时间':
                    time, '浏览量': num})
            print("第%d页保存成功"%i)
    #保存到本地json文件
    with open('./河南工学院招聘信息.json', 'w',encoding='utf-8') as fp:
        json.dump(info, fp=fp, ensure_ascii=False, indent=5)
    print('job信息保存成功')



