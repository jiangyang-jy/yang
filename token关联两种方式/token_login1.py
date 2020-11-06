#上一个接口的token传入有两种方式，不管网站还是app；
"""第一种，参数关联"""
import requests
s = requests.session()
def login(s, usr, pwd):
    url1 = "http://xxxxxxx"
    body = {
        "mobile": usr,
        "password": pwd
    }
    r1 = s.post(url1, json=body)
    #r1 = s.post(url1, json=json.dumps(body)) dumps是转字符串的，也可以说json；loads是转dict；
    print(r1.json())
    return r1.json()["data"]["token"]
    #return r1.json().get("data").get("token")不同的方式


def login_assets(s):
    url2 = "http://xxxxxxx"
    h = {"token": token}#参数关联，上个接口返回的token
    r2 = s.post(url2, headers=h)
    print(r2.json())


if __name__ == '__main__':
    # 把函数返回的值，用变量存起来，给下个接口使用
    token = login(s, "xxxxxxxxxxx", "12345678")
    login_assets(s)

