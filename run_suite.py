#1.导包
import unittest
from test_syu.test_login import TestLogin
#2.创建测试套件
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
#3.运行用例           #verbosity==级别==日记的详细程度
unittest.TextTestRunner(verbosity=2).run(suite)