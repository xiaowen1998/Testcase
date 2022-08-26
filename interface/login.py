"""s使用requests访问接口"""

import requests  # 可以发送http请求的包
import json  # 导入json，可以将json转换为字典


# 将接口链接中项目地址提出来
base_url = 'http://150.109.38.68/api/user/'

p = {
    'username': '1766353759@qq.com',
    'password': '123456789',
    'device_type': 'android',
    'client_id': '9',
    'client_secret': 'ruua6V1baBNfsc7Uld5gDTDlcytsZu2WyDbSKnOo',
    'grant_type': 'password'
}

r = requests.post(base_url + 'login', params=p)

print(r.text)  # 请求返回的数据
print(r.status_code)  # 状态码
# print(r.url)
# print(r.text['message'])#打印message的值
# print(r.text[37:44])#根据索引打印处message的值
# print(r.text['token'])
# print(r.text['data'])

re = json.loads(r.text)  # 将接口返回的json转换为字典型
print(re['message'])  # 转换后的re为字典类型
# print(re["data"])
print(re['data']['token_type'])  # 嵌套访问获取token到前缀
print(re['data']['access_token'])  # 嵌套访问获取token字符串