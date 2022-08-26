"""将每个接口封装为单独的方法"""
import requests  # 导入发送http请求的包
import json  # 导入可以将json转换为字典型的包
from config.headers import headers
from log import log_2   # 导入日志文件

# from nene_test.interface_test.Log import log   # 导入日志文件


class interface:
    def login(self, user, passwd):
        """封装登录接口
        :rtype: object
        """
        base_url = 'http://150.109.38.68/api/user/'  # 项目地址
        # 传入参数
        data = {
            'username': user,
            'password': passwd,
            'device_type': 'android',
            'client_id': '9',
            'client_secret': 'ruua6V1baBNfsc7Uld5gDTDlcytsZu2WyDbSKnOo',
            'grant_type': 'password'
        }
        r = requests.post(base_url + 'login', params=data)
        response = json.loads(r.text)  # 将接口返回的数据转换为字典
        # print(r.status_code)
        # print(response['message'])  # 打印message的值
        self.assertEqual('200', response['status_code'])
        log_2.log(response, 'info')
        return response

    def get_profile(self):
        """封装获取用户信息接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        # 加入请求头信息 self.headers = headers  # 调用headers文件内请求头信息 headers = { 'Accept': 'application/json',
        # 'Authorization': "Bearer
        # eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjBhNTM2MmYxZmE3NTJiN2FjODliMWFkNGQwNTY5M2FiYmFmZmM3NTgwNjYzOTgxYzkxOGQ0NmU0NWRiMTVkOGFlZmMyNmIwYTE1OWYzZjRiIn0.eyJhdWQiOiI5IiwianRpIjoiMGE1MzYyZjFmYTc1MmI3YWM4OWIxYWQ0ZDA1NjkzYWJiYWZmYzc1ODA2NjM5ODFjOTE4ZDQ2ZTQ1ZGIxNWQ4YWVmYzI2YjBhMTU5ZjNmNGIiLCJpYXQiOjE2MDg3OTk2OTEsIm5iZiI6MTYwODc5OTY5MSwiZXhwIjoxNjQwMzM1NjkxLCJzdWIiOiIyMzg1Iiwic2NvcGVzIjpbXX0.qlhmwfyk1RJO7YEWPx5P76OJM_RqfI5WAS5mWTOgjVL_UGs7zaJiMzuHmZJiJlOK0dEcpi0m-NpbPor5gqR-FCUJqkoWCKsshgD9ME6j1ZnZHD_7uEc16sqtnPYCbToTd0WqltvdzDggknCyUH815I22WxnxZ8A3HGdF2M-sKZoN8kZAzlw_ROWnUNHqQiyz6V-dgrVEXmGAWxBEg_4W_ZOxNeBXaEGrWbyIU-V_med_hJMWoUe26eTdDcRTytZFuUZNBBA9_TCcJWmxW9-Ugr-tEQ40O_FlksjYKsEUvMT9F8-NpshQlUKRiguUMa5fzvXCrpCnsVU25Jf9UPejFq26146zyqMenCjJnQyDCLWKDu3EGt5fsIRslRF47IvncSH9NCI80jkJSiMMyoUaheBuclGh2sEuoSqmwSopeHckQU5Wu5wLbQg-zK6d6yiqZmljO5YhWe2UepDifbT4hH6YwZD6qp-dD-W-2C1WDG2UGN6MJdLO6MqyrDeRyUB16e-hHvpEvpu5VfUFzdaca-z-8MjgPtspz2ML1iltlT6r7PwJeFdnA3BVGQGQ6kaASyNrMoB1f9uiJ3FaER3zSdwxEctPK14kuk3ss9LkPBuMtf4o2K-pmhK3CquGsUU6qUtlon-BqmPiVJ5SRY6C2XrWBFU_UiPmxdlfnB0VR70", }
        r = requests.get(base_url + 'get_profile', headers=headers)
        response = json.loads(r.text)  # 将接口返回的数据转换为字典
        # print(r.status_code)
        # print(response['message'])  # 打印message的值
        self.assertEqual('200', response['status_code'])
        log_2.log(response, 'info')
        return response

    def getUserBalanceLogs(self):
        """封装获取用户金币记录接口"""
        base_url = 'http://150.109.38.68/api/user/'
        # self.headers = headers  # 调用headers文件内请求头信息
        r = requests.post(base_url + 'getUserBalanceLogs', headers=headers)
        response = json.loads(r.text)  # 将接口返回的数据转换为字典
        # print(r.status_code)
        # print(response['message'])  # 打印message的值
        log_2.log(response, 'info')
        return response

    def find_match(self):
        """封装普通匹配接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        # self.headers = headers  # 调用headers文件内请求头信息
        r = requests.post(base_url + 'find_match', headers=headers)
        response = json.loads(r.text)  # 将接口返回的数据转换为字典型
        # print(r.status_code)
        # print(response['message'])  # 打印message的值
        self.assertEqual('200', response['status_code'])
        log_2.log(response, 'info')
        return response

    def product(self, pid, token):
        """封装用户内购记录接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        data = {
            'product_id': pid,
            'purchase_token': token
        }
        r = requests.post(base_url + 'product', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def instant_chat(self, pid):
        """ 封装即使匹配-添加为好友接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        data = {'chat_user_id': pid}
        r = requests.post(base_url + 'instant_chat', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def likes(self, status, like_id, data_type):
        """封装滑卡喜欢/不喜欢接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        data = {
            'status': status,  # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢
            'like_id': like_id,
            'data_type': data_type  # 0:普通匹配数据,1:精选匹配数据
        }
        r = requests.post(base_url + 'likes', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def instant_match(self, mismatch_user):
        """封装即使匹配接口"""
        base_url = 'http://150.109.38.68/api/user/v1/'
        data = {'mismatch_user': mismatch_user}
        r = requests.post(base_url + 'instant_match', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    # def find_match(self):
    #     """封装普通匹配接口"""
    #     base_url = 'http://150.109.38.68/api/user/v1/'
    #     # data = {}
    #     r = requests.post(base_url + 'find_match', headers=headers)
    #     response = json.loads(r.text)
    #     # print(r.status_code)
    #     # print(response['message'])
    #     log_test.log(response, 'info')
    #     return response

    def interact_remind(self, Type):
        """封装获取互动聊天消息提示接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'type': Type}
        r = requests.get(base_url + 'interact_remind', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def userOpinions(self, score, feedback):
        """封装获取用户反馈意见接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'score': score, 'feedback': feedback}
        r = requests.post(base_url + 'userOpinions', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def leaveRandomFormation(self, sz, zf):
        """封装离开随机视频列队接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'type': sz, 'unique_token': zf}
        r = requests.post(base_url + 'leaveRandomFormation', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def randomFormation(self, ty):
        """封装加入随机视频队列接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'type': ty}
        r = requests.post(base_url + 'randomFormation', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def populars(self, pa, pe):
        """封装精选视频接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'page': pa, 'per_page': pe}
        r = requests.get(base_url + 'populars', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def joinVideoRoom(self, unique_token):
        """封装加入房间接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'unique_token': unique_token}
        r = requests.post(base_url + 'joinVideoRoom', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def video_duration(self, s, uid, token, room):
        """封装视频扣费接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {
            'seconds': s,  # 时长（s）
            'like_id': uid,  # 通话对象id
            'video_unique_token': token,  # 视频唯一token
            'channel': room  # 房间号
        }
        r = requests.post(base_url + 'video_duration', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def video_logs(self):
        """封装视频消费/收入记录接口"""
        base_url = 'http://150.109.38.68/api/user/'
        r = requests.get(base_url + 'video_logs', headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def videoLikes(self, like_id, token):
        """封装视频喜欢接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'like_id': like_id, 'unique_token': token}
        r = requests.post(base_url + 'videoLikes', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def getAgoraVideoToken(self, token, Type):
        """封装获取声网token和房间信息接口"""
        base_url = 'http://150.109.38.68/api/user/'
        data = {'unique_token': token, 'chatType': Type}
        r = requests.post(base_url + 'getAgoraVideoToken', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response

    def settle_accounts(self, room, s, up_id):
        """封装精选视频结算接口"""
        base_url = 'http://150.109.38.68/api/user/video/'
        data = {
            'channel': room,
            'duration': s,
            'hung_up_id': up_id
        }
        r = requests.post(base_url + 'settle_accounts', params=data, headers=headers)
        response = json.loads(r.text)
        # print(r.status_code)
        # print(response['message'])
        log_2.log(response, 'info')
        return response


if __name__ == '__main__':
    inter = interface()  # 创建对像
    print(inter.login('1766353759@qq.com', 123456789))  # 调用登录的方法
    print(inter.get_profile())  # 打印获取到用户信息数据
    print(inter.getUserBalanceLogs())  # 打印获取到的用户金币记录数据
    print(inter.find_match())  # 打印获取到到用户普通匹配记录
    print(inter.product('coins_sale_45000',
                        'emndeckichndggooipfghdcj.AO-J1Oza6MeULgpsv'
                        '-xoQUKEPpWv_4U2OP38D8RXLRY0VSMXc9DJXbdptXOFANeBhifLDzLb2c0v4YKmXTBKvY '
                        '-jPouD4MalJA '
                        ))  # 打印用户内购记录
    print(inter.instant_chat(2312))  # 打印即使匹配
    print(inter.likes(1, 2312, 0))  # 打印滑卡喜欢到卡片
    print(inter.instant_match(22))  # 打印即使匹配结果
    print(inter.find_match())  # 打印普通匹配结果
    print(inter.interact_remind(1))
    print(inter.userOpinions(1, 'asd'))  # 打印获取用户反馈信息结果
    print(inter.leaveRandomFormation(1, 'db92972ca62a098273c395411025e77f'))  # 打印离开随机视频列队结果
    print(inter.randomFormation(1))  # 打印加入随机队列的结果
    print(inter.populars(1, 15))  # 打印精选视频
    print(inter.joinVideoRoom('58de775c9924f0788f88c28259e0b16b'))  # 打印加入房间结果
    print(
        inter.video_duration(60, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385'))  # 打印视频扣费结果
    print(inter.video_logs())  # 打印消费收入明细结果
    print(inter.videoLikes(2360, '42fc91f16d1401efdc7101c34ced770f'))  # 打印视频喜欢结果
    print(inter.getAgoraVideoToken('4cb4654156c2dea6086fb09f92ff0eaf', 1))  # 通话中才可请求到（call中）
    print(inter.settle_accounts('nene_1609919792833_2360_2385', 8, 2360))

    # if __name__ == '__main__':
    # inter = interface()  # 创建对像
