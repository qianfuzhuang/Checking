from selenium import webdriver
import time
import requests
headers={
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'referer':'https://user.qzone.qq.com/469422624',
'sec-fetch-dest':'script',
'sec-fetch-mode':'no-cors',
'sec-fetch-site':'cross-site',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.363',}
url='http://www.quanshuwang.com/'
driver = webdriver.Chrome()
# driver=driver.implicitly_wait(20)
driver.get(url)
driver.maximize_window()


def read():

    # time.sleep(10)
    # '<input name="searchkey" type="text" id="bdcsMain" onfocus="this.classname='over';if (value =='这是一个神奇的搜索'){value =''}" onblur="this.classname='input'" value="这是一个神奇的搜索">'
    # driver.find_element_by_xpath()
    # driver.find_element_by_class_name()
    
    driver.find_element_by_name('searchkey').send_keys('雪中悍刀行')
    '<input type="image" name="searchbuttom" id="searchbuttom" src="/kukuku/images/search.jpg">'
    driver.find_element_by_name('searchbuttom').click()
    # 此时滚动条滚动得是第一个页面
    driver.switch_to.window(driver.window_handles[1])
    '<a href="http://www.quanshuwang.com/book/15/15228" class="reader" title="雪中悍刀行免费阅读">开始阅读</a>'
    # js = 'document.documentElement.scrollTop=10000'
    js = "var q=document.documentElement.scrollTop=500"
    driver.execute_script(js)
    js2 = "var q=document.documentElement.scrollLeft=10"
    driver.execute_script(js2)
    # time.sleep(5)
    driver.find_element_by_class_name('reader').click()
    time.sleep(5)


if __name__ == '__main__':
    read()
    # 测试前进后退
    # time.sleep(5)
    # driver.back()
    # time.sleep(5)
    # driver.forward()
    # driver.quit()
    driver.switch_to.window(driver.window_handles[1])
    js3 = "var q=document.documentElement.scrollLeft=100"
    driver.execute_script(js3)
    driver.find_element_by_name('username').send_keys('故渊池鱼')
    driver.find_element_by_name('password').send_keys('12345678as')
    driver.find_element_by_name('submit').click()

    time.sleep(10)


