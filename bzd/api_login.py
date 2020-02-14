# 3.请求IHRM系统的用户列表接口：http://182.92.81.159/api/sys/user?page=1&size=1，提示：需要先登录
# 要求：
#
# - 被测接口和测试用例进行分离
# - 断言以下俩个个值：
#   - code
#   - mobile
# - 放在一个脚本进行统一运行，提示：把测试脚本放在run_suite.py
import requests

from bzd.comfig import headers_da


class ApiLogin():
    def __init__(self):
        # 定义登陆url
        self.url_login = "http://182.92.81.159/api/sys/login"
        self.user_url = "http://182.92.81.159/api/sys/user?page=1&size=1"
        self.url_ihrm = "http://182.92.81.159/api/sys/profile"

    # 登陆
    def api_logint(self, mobile, password):
        # 定义测试数据
        data = {"mobile": mobile, "password": password}
        # 调用post方法,返回
        result = requests.post(self.url_login, json=data).json()
        data_str = result.get("data")
        token = "Bearer " + data_str
        headers_da["Authorization"] = token
        return headers_da

        # 用户列表

    def user_list(self, headers_da):
        try:
            return requests.get(self.user_url, headers=headers_da).json()
        except Exception as e:
            print("请求用户列表接口数据异常".format(e))

    # 用户信息
    def ihrm_user(self, headers_da):
        try:
            return requests.post(self.url_ihrm, headers=headers_da).json()
        except Exception as e:
            print("请求ihrm用户信息接口数据异常".format(e))
