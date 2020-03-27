from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import urllib.request
import urllib.parse
import json

zhanghao = input("输入你的学号：")

req_url = "http://yiqing.hnevc.com/"
chrome_options=Options()

chrome_options.add_argument('--headless') #隐藏浏览器访问
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get(req_url)
browser.find_element_by_xpath("//*[@id='username']").send_keys(zhanghao) #输入账号
browser.find_element_by_xpath("//*[@id='password']").send_keys("123456") #输入密码
browser.find_element_by_xpath("//*[@onclick='login()']").click() #点击登录

cookies = browser.get_cookies() #获取cookies
str = str(cookies)

browser.close()
browser.quit() #关闭浏览器进程

pattern = re.compile('[A-Za-z0-9]{32}')#正则表达
cookies = (pattern.search(str).group(0)) #筛选出cookies并赋值到cookies

print(cookies)
