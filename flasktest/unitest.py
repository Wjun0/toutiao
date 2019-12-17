import json
import unittest

# 在flask项目中的测试配置，settings.py文件
# from toutiao import create_falsk_app
# class TestingConfig(DefaultConfig):
#     TESTING = True
#     #开启测试模式，flask就不会内部继续异常捕获，方便查询具体的报错位置
#
# config_dict ={
#     'dev':DefaultConfig,
#     'test':TestingConfig
# }


class SuggestionTestCase(unittest.TestCase):
    def setUp(self):
        '''初始化，每个测试方法前会调用'''
        print('初始化')
    def tearDown(self):
        '''每个方法执行后会调用'''
        print('测试结尾的资源回收')

    def test_request_normal(self):
        '''测试正常请求'''
        # print('测试正常请求')
        # self.assertEqual(1,2,'1 !=2')

        '''测试中发请求 
            1，使用urllib/requests
            2，使用web框架提供测试的工具  
                优点：不是真实的发请求，只是模拟请求，提高测试效率，不会有网络延迟
        '''
        #发起测试的请求
        res = self.client.get('/v1_0/suggestion?q=python%20web')

        #对状态码进行断言
        self.assertEqual(res.status_code,200,'正常请求的状态码是200')

        #对数据进行断言
        res_json_str = res.data
        resp_dict = json.loads(res_json_str)
        self.assertIn('message',resp_dict,'正常返回的数据不包含message')
        self.assertIn('data',resp_dict,'正常返回的数据不包含data字段')

        data = resp_dict['data']
        self.assertIn('options',data,'返回数据的data字段中不包含option字段')



    def test_param_q_missing(self):
        print('测试参数缺失')
        res = self.client.get('/v1_0/suggestion')
        self.assertEqual(res.status_code, 400, '状态码不是500')

    def test_param_q_length_error(self):
        print('测试参数q的长度错误')


if __name__ == '__main__':
    unittest.main()

