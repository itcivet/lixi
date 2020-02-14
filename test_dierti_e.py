"""
# 1.请求该地址的登录接口：http://dev-www.zcbk.deayou.com/member/public/login，
# 请求体数据：{"keywords":"13210001000","password":"123qwe"} 。请求体类型为form
#
# 要求：能请求成功,返回数据如下：
#
# {"status":200,"description":"登录成功"}
# url = "http://dev-www.zcbk.deayou.com/member/public/login"
# data = {"keywords":"13210001000","password":"123qwe"}
# rues = requests.post(url=url,data=data)
# print(rues.json())

"""

# 2.通过代码请求IHRM系统的用户资料接口：http://182.92.81.159/api/sys/profile，提示：需要先登录
# 要求：
# - 要对返回结果的mobile进行断言，
# - 同时要对返回值中apis中的“电饭锅电饭锅”进行断言
#   1. 返回结果的部分片段包括 ： "apis": [
#
#   ​        "API-USER-DELETE",
#
#   ​        "电饭锅电饭锅"
#
#   ​      ]

import unittest
from pprint import pprint
import requests
# 请求IHRM系统的用户资料接口

class TestHirm(unittest.TestCase):
    headers_da = {}
    @classmethod
    def setUpClass(cls) -> None:
        data = {"mobile": "13800000002", "password": "123456"}
        r = requests.post("http://182.92.81.159/api/sys/login", json=data).json()
        print("登录返回数据:{}".format(r))
        str_data = r.get("data")
        token = "Bearer " + str_data
        TestHirm.headers_da["Authorization"] = token
        print(TestHirm.headers_da)

    def test_v(self):
        #请求接口
        re = requests.post("http://182.92.81.159/api/sys/profile", headers=TestHirm.headers_da).json()
        # print(re)
        pprint(re)
        # - 要对返回结果的mobile进行断言，
        # - 同时要对返回值中apis中的“电饭锅电饭锅”进行断言
        self.assertEqual("13800000002",re.get("data").get("mobile"))
        self.assertEqual("电饭锅电饭锅",re.get("data").get("roles").get("apis")[1])
