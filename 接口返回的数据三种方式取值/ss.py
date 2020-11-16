from kecheng.ke7.ai_login import login
import json
import re
import jsonpath
"""'{"code":200,"msg":"success","data":{"token":"b33f1bd1e49abc7579c743e89f8ba2b9"}}'"""
fanhui = login()

# 第一种方式：re取token
token0 = re.findall('"token":"(.+?)"', fanhui)
print(token0[0])

# 第二种方式：字典取token(可以直接.json())
str_dict = json.loads(fanhui)
token1 = str_dict["data"]["token"]
print(token1)

# 第三种方式：jsonpath取token($根节点，第一层  .子节点，第二层 ..相对节点，不管第几层  没有取到返回False)
token2 = jsonpath.jsonpath(str_dict, "$..token")
print(token2[0])

if __name__ == '__main__':
    import os
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "ss.py")
    print(path)