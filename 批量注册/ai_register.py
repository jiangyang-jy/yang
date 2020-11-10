"""批量注册：取token、id"""
import requests
import os
filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "token.txt")#获取token.txt的路径，必须在同一个项目里
url = 'http://xxxxx'
s = requests.session()


def xiu_register(s):
#两层循序乘积=次数
    for i in range(2):
        for j in range(1):
            mobile = "151797593"+str(i)+str(j)
            body = {
                "mobile": mobile,
                "code": "123456",
                "password": "12345678",
                "invite_code": "59201427"
            }
            r = s.post(url, json=body)
            print(r.json())
            token = r.json()['data']['token']
            print(token)
            id = str(r.json()["data"]["id"])
            print(id)
            #追加的方式，把token写入文件中
            with open(filepath, 'a') as fp:
                fp.write(token+"\n")


if __name__ == '__main__':
    xiu_register(s)
