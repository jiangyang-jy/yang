import requests
import pytest
import os
from case.read_yaml import get_yaml
s = requests.Session()
url = "http://api.shopip.caisxs.com/user/login"
yaml_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_data.yml")
print(f"读取到文件地址：{yaml_file}")
test_data = get_yaml(yaml_file)


class Test_login():

    """登录成功"""
    @pytest.mark.parametrize("test_input, expect", test_data)
    def test_login_1(self, test_input, expect):
        r = s.post(url, json=test_input)
        print(r.text)
        assert r.json()["msg"] == expect["msg"]

    # """登录失败,手机号为空"""
    # @pytest.mark.parametrize("test_input, expect", test_data)
    # def test_login_3(self, test_input, expect):
    #     r = s.post(url, json=test_input)
    #     print(r.text)
    #     assert r.json()["code"] == expect["code"]

    # """登录失败,密码为空"""
    # def test_login_4(self):
    #     body = {
    #         "device_type": "ios",
    #         "device_number": "3517033688244",
    #         "mobile": "19842314796",
    #         "code": "",
    #     }
    #     r = s.post(url, json=body)
    #     print(r.text)
    #     assert r"\u8bf7\u8f93\u5165\u5bc6\u7801|\u9a8c\u8bc1\u7801" in r.text
    #
    # """登录失败,设备为空"""
    # def test_login_5(self):
    #     body = {
    #         "device_type": "",
    #         "device_number": "3517033688244",
    #         "mobile": "19842314796",
    #         "code": "qQ123456",
    #     }
    #     r = s.post(url, json=body)
    #     print(r.text)
    #     assert r"\u7f3a\u5c11\u8bbe\u5907\u7c7b\u578b" in r.text
    #
    # """登录失败,设备号为空"""
    # def test_login_6(self):
    #     body = {
    #         "device_type": "Android",
    #         "device_number": "",
    #         "mobile": "19842314796",
    #         "code": "qQ123456",
    #     }
    #     r = s.post(url, json=body)
    #     print(r.text)
    #     assert r"dev_\u7f3a\u5c11\u8bbe\u5907\u7f16\u7801" in r.text


