import unittest
from bzd.api_login import ApiLogin
from bzd.comfig import headers_da


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = ApiLogin()
        headers_da = cls.api.api_logint("13800000002","123456")
        # print(headers_da)
    # 测试用户列表
    def test_g(self):
        #请求用户列表接口
        r = self.api.user_list(headers_da)
        print(r)
        #断言\

    # # 测试用户信息接口
    def test_a(self):
    #请求用户信息接口
        r = self.api.ihrm_user(headers_da)
        print(r)
    # 断言
