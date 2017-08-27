# coding=utf-8  
import os
import time
from selenium import webdriver

#打开火狐浏览器 V55
driver = webdriver.Firefox()#打开火狐浏览器
url = "http://www.csdn.net/"#这里打开CSDN网站
driver.get(url)#设置火狐浏览器打开的网址
time.sleep(2)

#xpath路径定位  导航栏
elem_dh = driver.find_elements_by_xpath("//div[@class='menu']/ul/li/a")
time.sleep(5)

#获取当前窗口句柄
now_handle = driver.current_window_handle 
print (now_handle)#打印窗口句柄  是一串数字
time.sleep(10)

#循环获取界面
for elem in elem_dh:
    print (elem.text)                    #获取元素的文本值
    print (elem.get_attribute('href'))   #获取元素的href属性值
    elem.click()#点击进入新的界面 _blank弹出

    #获取所有窗口句柄
    all_handles = driver.window_handles#获取窗体句柄，已经有两个窗体了
    #print (all_handles)
    
    #弹出两个界面,跳转到不是主窗体界面
    for handle in all_handles:
        if handle!=now_handle:   
            #输出待选择的窗口句柄
            print (handle)
            driver.switch_to_window(handle)#选择非主窗体句柄值的窗口
            time.sleep(10)

            print (u'弹出界面信息')
            print (driver.current_url)#获取当前页面的Url函数
            print (driver.title)#获取当前页面的title值
            time.sleep(10)

            #获取登录连接信息
            elem_sub = driver.find_element_by_xpath("//ul[@class='btns']/li/a")
            print (elem_sub.text)#获取元素的文本值 打印登录二字
            print (elem_sub.get_attribute('href'))#获取元素的href属性值
            print ('')
            time.sleep(10)

            #关闭当前窗口
            driver.close()
            

            #输出主窗口句柄
            print (now_handle)
            driver.switch_to_window(now_handle) #返回主窗口 开始下一个循环跳转