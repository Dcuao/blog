# coding=utf-8

import requests
import json
import unittest


class UploadTest(unittest.TestCase):
    """
    请求上传视频的接口
    """
    def test_upload(self):
        """
        test case
        :return:
        """
        url = 'http://v.polyv.net/uc/services/rest?method=uploadfile'
        jsonrpc = "{\"title\": \"标题yzc0116\", \"tag\":\"标签yzc0116\",\"desc\":\"描述yzc0116\"}"
        filepath = 'C:\\Users\\yangzc\\Desktop\\FlickAnimation.avi'
        # 打开文件
        fo = open(filepath, 'rb')
        # video表示实际的文件参数
        video = {'Filedata': fo}
        # params表示实际的参数列表，包括：writetoken和JSONRPC这两个参数
        params = {'writetoken': '7043f898-8322-4e39-8bb5-7956bf0eb641', 'JSONRPC': jsonrpc}
        response = requests.post(url, data=params, files=video)
        print(response.text)
        # self.assertEqual("{\"error\":\"0\"}", response.text)
        entity = json.loads(response.text)
        self.assertEqual(0, int(entity['error']))
        # 关闭文件
        fo.close()


'''
第二部操作
'''


'''
进行第三次操作
'''

'''
进行第四次操作
'''

'''
第五修改
'''

'''
一次性操作
'''

'''
mac  第一次操作

'''