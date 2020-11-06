#上一个接口的token传入有两种方式，不管网站还是app；
"""第二种，把token更新到头部，用s去传"""
import requests
s = requests.session()


def login(s, usr, pwd):
    url1 = "http://xxxxxxx"
    body = {
        "mobile": usr,
        "password": pwd
    }
    r1 = s.post(url1, json=body)
    print(r1.json())
    token = r1.json()["data"]["token"]
    c = {"token": token}
    s.headers.update(c) #把token更新到headers里，后面的请求，直接s传过去


def login_assets(s):
    url2 = "http://xxxxxxx"
    r2 = s.post(url2)
    print(r2.json())


if __name__ == '__main__':
    login(s, "xxxxxxxxxxx", "12345678")
    login_assets(s)


