import requests
from case.login.mall_login import login_get_token
s = requests.Session()
url = "http://api.shopip.caisxs.com/user/editUserInfo"
token = login_get_token()
h = {"token": token}

class TestInfo():

    """修改昵称成功"""
    def test_info_1(self):
        body = {
            "key": "nickname",
            "value": "仿真草sm"
        }
        r = s.post(url, json=body, headers=h)
        print(r.text)
        assert r"\u4eff\u771f\u8349sm" in r.text
        

    """修改性别男成功"""
    def test_info_2(self):
        body = {
            "key": "sex",
            "value": "1"
        }
        r = s.post(url, json=body, headers=h)
        print(r.text)
        assert "dev_success" in r.text

    """修改性别女成功"""
    def test_info_3(self):
        body = {
            "key": "sex",
            "value": "2"
        }
        r = s.post(url, json=body, headers=h)
        print(r.text)
        assert "dev_success" in r.text

    """修改个性签名成功"""
    def test_info_4(self):
        body = {
            "key": "sign",
            "value": "zz\n"
        }
        r = s.post(url, json=body, headers=h)
        print(r.text)
        assert "dev_success" in r.text
