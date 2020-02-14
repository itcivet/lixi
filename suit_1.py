#1.导包
import unittest
from HTMLTestRunner import HTMLTestRunner
#组装测试套件
suit  = unittest.defaultTestLoader.discover("./test_syu",pattern="test*.py")
#3.获取报告存储路径,实例化htmlrunner 调用run
with open("./report/baogao.html","wb")as f:
    HTMLTestRunner(stream=f).run(suit)