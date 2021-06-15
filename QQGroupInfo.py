from selenium import webdriver
from lxml import etree
import csv
import time
fp = open('./qq群信息.csv', mode='w', encoding='utf-8-sig',newline='')
csv_writer = csv.writer(fp,dialect='excel')
csv_writer.writerow(['成员数','群成员昵称','群名片','QQ号', '性别', 'QQ龄','入群时间' ,'等级' ,'最后发言'])

url = 'https://qun.qq.com/member.html#gid=87683192'

def info():
    for i in result:

        # 第number个成员
        number = i.xpath('./td[2]/text()')[0].strip()
        # 群成员昵称
        name = i.xpath('./td[3]/span/text()')[0].strip()
        # 群名片
        member = i.xpath('./td[4]/span/text()')[0].strip()
        if member.strip() == '':
            member='空'
        # qq号
        qq = i.xpath('./td[5]/text()')[0].strip()
        # 性别
        sex = i.xpath('./td[6]/text()')[0].strip()
        # qq龄
        year = i.xpath('./td[7]/text()')[0].strip()
        # 入群时间
        intotime = i.xpath('./td[8]/text()')[0].strip()

        # 等级（积分）
        grade = i.xpath('./td[9]/text()')[0].strip()
        # 最后发言
        endspeaktime = i.xpath('./td[10]/text()')[0].strip()
        csv_writer.writerow([number, name, member, qq, sex, year, intotime, grade, endspeaktime])
    fp.close()

def sourse():
    global f
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(url)

    js="var q=document.documentElement.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(10)
    # 获取源码
    res = driver.page_source
    # 关闭浏览器
    driver.quit()
    # 保存源码
    with open('qqhtml.txt', 'w', encoding='utf-8') as f:
        f.write(res)
    f.close()

def list():
    global f, result
    with open('qqhtml.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    html = etree.HTML(content)
    result = html.xpath('//*[@id="groupMember"]/tbody[@class="list"]/tr')

if __name__ == '__main__':
    sourse()
    list()
    info()







