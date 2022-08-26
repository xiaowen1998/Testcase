import requests
import json

base_url = "http://dev.auth.authority-account.172.16.90.27.xip.io/account/"


p = {
    'username': 'T6001314',
    'password': 'YANGpeng2128##',
    'ididm': '1',
    'deviceinfo': 'pc',
    'systemid': '33',
    'timestamp': '1616492823214'
}

r = requests.post(base_url + 'login', params=p)

print(r.text)  # 请求返回的数据
print(r.status_code)  # 状态码



