"""博客园绕过登陆，访问登陆后的页面：方式二自动获取cookie"""
#前提，关闭浏览器，再次打开是已登录的状态，也就是适用cookie机制的
#静默模式运行，无法加载缓存。
from selenium import webdriver
import requests
import time
import urllib3
urllib3.disable_warnings()
s = requests.session()
s.verify = False

def get_cook():
    option = webdriver.ChromeOptions()
    #option.add_argument("headless")#
    option.add_argument(r"--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data")
    driver = webdriver.Chrome(options=option)
    driver.get("https://home.cnblogs.com/")
    driver.maximize_window()
    cookies = driver.get_cookies()#获取cookie
    print(cookies)
    time.sleep(3)
    driver.quit()
    return cookies

def cnblog_fatie(cookies):
    c = requests.cookies.RequestsCookieJar()
    for i in cookies:
        c.set(i["name"], i["value"])
    s.cookies.update(c)
    print(c)
    url = "https://home.cnblogs.com/ajax/ing/Publish"
    h = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/json; charset=UTF-8"
    }
    body = {
        "content": "hello",
        "publicFlag": 1
    }
    r = s.post(url, json=body, headers=h)
    print(r.json())

if __name__ == '__main__':
    a = get_cook()
    cnblog_fatie(a)


