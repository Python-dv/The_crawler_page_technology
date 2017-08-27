# coding=utf-8  
import os
import time
from selenium import webdriver

#打开火狐浏览器 需要V47版本以上的
driver = webdriver.Firefox()#打开火狐浏览器
url = "http://www.ecit-it.com/plus/list.php?tid=33"#这里打开我的博客网站
driver.get(url)#设置火狐浏览器打开的网址
time.sleep(2)

#获取当前窗口句柄
now_handle = driver.current_window_handle #获取当前窗口句柄
print ("我是当前窗口的句柄:",now_handle)#打印窗口句柄  是一串数字
time.sleep(10)

for i in range(10):
    elem_dh = driver.find_elements_by_xpath("//div[@class='dede_pages']/ul/li/a")
    for elem in elem_dh:
        if elem.text == "下一页":
            print ("我是下一页按钮上的文本信息:",elem.text)                    #获取元素的文本值
            print ("我是下一页按钮的地址",elem.get_attribute('href'))   #获取元素的href属性值
            elem.click()#点击进入新的界面 _blank弹出
            print ("刚点击下一页完成了！")
        
time.sleep(20)
