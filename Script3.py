# coding=utf-8  
import os
import time
from selenium import webdriver

#打开火狐浏览器 需要V47版本以上的
driver = webdriver.Firefox()#打开火狐浏览器
url = "http://codelife.ecit-it.com"#这里打开我的博客网站
driver.get(url)#设置火狐浏览器打开的网址
time.sleep(2)

#使用xpath进行多路径或多元素定位,用法看官网http://selenium-python.readthedocs.io/locating-elements.html
elem_dh = driver.find_elements_by_xpath("//div[@class='pagination pagination-large']/ul/li/a")
print ("我是刚获取的翻页按钮的路径数组:",elem_dh)
print ("下一页按钮元素：",elem_dh[2])
time.sleep(5)

#获取当前窗口句柄
now_handle = driver.current_window_handle #获取当前窗口句柄
print ("我是当前窗口的句柄:",now_handle)#打印窗口句柄  是一串数字
time.sleep(10)

#循环获取界面
for elem in elem_dh:
    if elem == elem_dh[2]:
        sum=0
        for i in range(10):
            print ("我是下一页按钮上的文本信息:",elem.text)                    #获取元素的文本值
            print ("我是下一页按钮的地址",elem.get_attribute('href'))   #获取元素的href属性值
            elem.click()#点击进入新的界面 _blank弹出
            print ("刚点击下一页完成了！")
            sum=sum+i
        print("你总共点击下一页已经10次了",sum)

time.sleep(20)