"""测试nene接口"""
# 导入封装好的接口方法
from interface.interface import interface  # 导入封装接口的文件
import unittest  # 导入单元测试框架
import warnings  # warnings库来忽略掉相关告警
from log import log_2


class Test_all(unittest.TestCase):  # 定义测试用例类
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        global inter  # 声明全局变量
        inter = interface()
        print("测试登录接口")

    def test_Test_login_1(self):
        """测试登录接口--正例"""
        # re = inter.login()
        re = inter.login('1766353759@qq.com', 123456789)  # 调用登录接口，输入账户密码
        # r = inter.login('1766353759@qq.com', re['auth'])#调用接口并返回数据
        self.assertEqual('200', re['status_code'])  # 断言判断

        # print(re)

    def test_Test_login_2(self):
        """测试登录接口--反例"""
        re = inter.login('1766353759@qq.com', 'lxw123456')  # 调用登录接口，输入错误密码
        self.assertEqual('The user credentials were incorrect.', re['message'])  # 断言判断
        # print(re)

    def test_Test_login_3(self):
        """测试登录接口--反例"""
        re = inter.login('1766353759q.com', '123456789')  # 调用登录接口，输入不存在的用户
        self.assertEqual('account not exist', re['message'])  # 断言判断
        # print(re)

    def test_get_profile(self):
        """测试获取用户信息接口"""
        # inter.login('1766353759@qq.com', 123456789)  # 调用登陆接口
        re = inter.get_profile()
        self.assertEqual('success', re['message'])
        # print(re)

    def test_getUserBalanceLogs(self):
        """测试获取用户金币记录接口"""
        re = inter.getUserBalanceLogs()
        self.assertEqual('success', re['message'])
        # print(re)

    def test_find_match(self):
        """测试普通匹配接口"""
        re = inter.find_match()
        self.assertEqual('success', re['message'])
        # print(re)

    def test_product_1(self):
        """测试用户内购记录接口--正例"""
        """传入正确的product_id和商品token"""
        re = inter.product('coins_sale_45000',
                           'emndeckichndggooipfghdcj.AO-J1Oza6MeULgpsv-xoQUKEPpWv_4U2OP38D8RXLRY0VSMXc9DJXbdptXOFANeBhifLDzLb2c0v4YKmXTBKvY-jPouD4MalJA')
        self.assertEqual('query product not find', re['message'])
        print(re)

    def test_product_2(self):
        """测试用户内购记录接口--反例"""
        """传入错误的product_id"""
        re = inter.product('coins_sale_45',
                           'emndeckichndggooipfghdcj.AO-J1Oza6MeULgpsv-xoQUKEPpWv_4U2OP38D8RXLRY0VSMXc9DJXbdptXOFANeBhifLDzLb2c0v4YKmXTBKvY-jPouD4MalJA')
        self.assertEqual('query product not find', re['message'])
        # print(re)

    def test_product_3(self):
        """测试用户内购记录接口--反例"""
        """传入空的product_id"""
        re = inter.product('',
                           'emndeckichndggooipfghdcj.AO-J1Oza6MeULgpsv-xoQUKEPpWv_4U2OP38D8RXLRY0VSMXc9DJXbdptXOFANeBhifLDzLb2c0v4YKmXTBKvY-jPouD4MalJA')
        self.assertEqual('The product id field is required.', re['message'])  # 判断商品ID为必传
        # print(re)

    def test_product_4(self):
        """测试用户内购记录接口--反例"""
        """传入错误的商品token"""
        re = inter.product('coins_sale_45000', 'abcdefg123')
        self.assertEqual('query product not find', re['message'])  # 判断商品ID为必传
        # print(re)

    def test_product_5(self):
        """测试用户内购记录接口--反例"""
        """传入空的商品token"""
        re = inter.product('coins_sale_45000', '')
        self.assertEqual('The purchase token field is required.', re['message'])  # 判断商品ID为必传
        # print(re)

    def test_instant_chat(self):
        """测试即时匹配-添加为好友--正例"""
        """传入错误的用户ID"""
        """客户端相互匹配到来之后才会请求这个接口，直接请求都是匹配失败到结果"""
        re = inter.instant_chat(2212)
        self.assertEqual('Matching fail', re['message'])

    def test_likes_1(self):
        """测试滑卡喜欢/不喜欢--正例"""
        """都传入正确都参数"""
        re = inter.likes(1, 2401, 0)  # # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢，  # 0:普通匹配数据,1:精选匹配数据
        self.assertEqual('User liked successfully', re['message'])

    def test_likes_2(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """传入已经是朋友的ID"""
        re = inter.likes(1, 2212, 0)
        self.assertEqual('You and 2212 already friend', re['message'])

    def test_likes_3(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """传入错误的用户ID"""
        re = inter.likes(1, 12, 0)
        self.assertEqual('The selected like id is invalid.', re['message'])

    def test_likes_4(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """传入字母ID"""
        re = inter.likes(1, 'ABC', 0)
        self.assertEqual('The like id must be an integer.', re['message'])

    def test_likes_5(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """第一个参数传入错误的值（超出设定范围的值）"""
        re = inter.likes(6, 2401, 0)
        self.assertEqual('', re['message'])

    def test_likes_6(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """第3个参数传入错误的值（超出设定范围的值）"""
        re = inter.likes(1, 2401, 2)
        self.assertEqual('User liked successfully', re['message'])

    def test_likes_7(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """第3个参数传入错误的值（超出设定范围的值）"""
        re = inter.likes(1, 2401, 2)
        self.assertEqual('User liked successfully', re['message'])

    def test_likes_8(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """第2个参数传入字符串（超出设定范围的值）"""
        re = inter.likes('asd', 2401, 2)
        self.assertEqual('', re['message'])

    def test_likes_9(self):
        """测试滑卡喜欢/不喜欢--反例"""
        """第3个参数传入字符串（超出设定范围的值）"""
        re = inter.likes(1, 2401, 'asd123')
        self.assertEqual('User liked successfully', re['message'])

    def test_likes_10(self):
        """测试滑卡喜欢/不喜欢--正例"""
        """都传入正确都参数"""
        re = inter.likes(2, 2401, 0)  # # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢，  # 0:普通匹配数据,1:精选匹配数据
        self.assertEqual('User superliked successfully', re['message'])

    def test_likes_11(self):
        """测试滑卡喜欢/不喜欢--正例"""
        """都传入正确都参数"""
        re = inter.likes(3, 2401, 0)  # # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢，  # 0:普通匹配数据,1:精选匹配数据
        self.assertEqual('User disliked successfully', re['message'])

    def test_likes_12(self):
        """测试滑卡喜欢/不喜欢--正例"""
        """都传入正确都参数"""
        re = inter.likes(4, 2401, 0)  # # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢，  # 0:普通匹配数据,1:精选匹配数据
        self.assertEqual('User liked successfully', re['message'])

    def test_likes_13(self):
        """测试滑卡喜欢/不喜欢--正例"""
        """都传入正确都参数"""
        re = inter.likes(5, 2401, 0)  # # 1:喜欢,2:超级喜欢,3:不喜欢,4:对方超级喜欢,5:对方超级不喜欢，  # 0:普通匹配数据,1:精选匹配数据
        self.assertEqual('User disliked successfully', re['message'])

    def test_instant_match_1(self):
        """测试即时匹配--正例"""
        """传入正确的参数值"""
        re = inter.instant_match(22)
        self.assertEqual('User instantMatch successfully', re['message'])

    def test_instant_match_2(self):
        """测试即时匹配--反例"""
        """传入字符串"""
        re = inter.instant_match('abc123')
        self.assertEqual('User instantMatch successfully', re['message'])

    def test_find_match_1(self):
        """测试普通匹配--正例"""
        re = inter.find_match()
        self.assertEqual('success', re['message'])

    def test_interact_remind_1(self):
        """测试获取互动聊天提示--正例"""
        """传入正确的参数"""
        re = inter.interact_remind(1)
        self.assertEqual('success', re['message'])

    def test_interact_remind_2(self):
        """测试获取互动聊天提示--正例"""
        """传入正确的参数"""
        re = inter.interact_remind(2)
        self.assertEqual('success', re['message'])

    def test_interact_remind_3(self):
        """测试获取互动聊天提示--反例"""
        """传入超出范围的参数值"""
        re = inter.interact_remind(3)
        self.assertEqual('The selected type is invalid.', re['message'])

    def test_userOpinions_1(self):
        """测试获取用户反馈意见"""
        """都传入正常都数据(参数无任何限制，可以随意输入)"""
        re = inter.userOpinions('abcd的咖啡喝的可乐放假啊都是开飞机啊看到了更好efgbgggghhhhhhjjj', 123)
        self.assertEqual('success', re['message'])

    def test_leaveRandomFormation_1(self):
        """测试离开随机视频列队--正例"""
        """都传入正常都参数（两个参数无限制，可随意输入）"""
        re = inter.leaveRandomFormation(1, 'abc')
        self.assertEqual('leave_success', re['message'])

    def test_leaveRandomFormation_2(self):
        """测试离开随机视频列队--反例"""
        """传入错误都参数"""
        re = inter.leaveRandomFormation(3, 'abc')
        self.assertEqual('leave_success', re['message'])

    def test_leaveRandomFormation_3(self):
        """测试离开随机视频列队--反例"""
        """传入错误都参数字符串"""
        re = inter.leaveRandomFormation('2abc', 'abc')
        self.assertEqual('leave_success', re['message'])

    def test_randomFormation_1(self):
        """测试加入随机视频队列--正例"""
        """传入正常参数"""
        re = inter.randomFormation(1)
        self.assertEqual('join_success', re['message'])

    def test_randomFormation_2(self):
        """测试加入随机视频队列--反例"""
        """随意输入字符串"""
        re = inter.randomFormation('ABC的孤独感123')
        self.assertEqual('join_success', re['message'])

    def test_populars_1(self):
        """测试精选视频接口--正例"""
        """输入正常参数值"""
        re = inter.populars(1, 15)
        self.assertEqual('success', re['message'])

    def test_populars_2(self):
        """测试精选视频接口--反例"""
        """随意输入各种字符串"""
        re = inter.populars('1', '0oklp')
        self.assertEqual('A non well formed numeric value encountered', re['message'])

    def test_populars_3(self):
        """测试精选视频接口--反例"""
        """输入错误都参数"""
        re = inter.populars('1abc', 15)
        self.assertEqual('success', re['message'])

    def test_jsonVideoRoom_1(self):
        """测试加入房间接口--正例"""
        """传入正确的unique_token"""
        re = inter.joinVideoRoom('58de775c9924f0788f88c28259e0b16b')
        self.assertEqual('join_success', re['message'])

    def test_jsonVideoRoom_2(self):
        """测试加入房间接口--反例"""
        """传入错误的unique_token"""
        re = inter.joinVideoRoom('de775c9924f0788f88c28259e0b16b')
        self.assertEqual('join_fail', re['message'])

    def test_jsonVideoRoom_3(self):
        """测试加入房间接口--反例"""
        """传入空unique_token"""
        re = inter.joinVideoRoom('')
        self.assertEqual('The unique token field is required.', re['message'])

    def test_video_duration_1(self):
        """测试视频过程中扣费--正例"""
        """传入正常参数"""
        re = inter.video_duration(60, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('decrement success', re['message'])

    def test_video_duration_2(self):
        """测试视频过程中扣费--反例"""
        """传入0时间"""
        re = inter.video_duration(0, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('The seconds must be at least 1.', re['message'])

    def test_video_duration_3(self):
        """测试视频过程中扣费--反例"""
        """传入小数时间"""
        re = inter.video_duration(0.30, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('The seconds must be an integer.', re['message'])

    def test_video_duration_4(self):
        """测试视频过程中扣费--反例"""
        """传入错误的ID"""
        re = inter.video_duration(60, 22, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('decrement success', re['message'])

    def test_video_duration_5(self):
        """测试视频过程中扣费--反例"""
        """传入空的ID"""
        re = inter.video_duration(60, '', '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('decrement success', re['message'])

    def test_video_duration_6(self):
        """测试视频过程中扣费--反例"""
        """传入错误的视频token"""
        re = inter.video_duration(60, 2360, 'ABC4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('The selected video unique token is invalid.', re['message'])

    def test_video_duration_7(self):
        """测试视频过程中扣费--反例"""
        """传入错误的房间号"""
        re = inter.video_duration(60, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2361_2385')
        self.assertEqual('The selected channel is invalid.', re['message'])

    def test_video_duration_8(self):
        """测试视频过程中扣费--反例"""
        """传入小数时间以及错误的token"""
        re = inter.video_duration(0.60, 2360, 'abc4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('The seconds must be an integer.', re['message'])

    def test_video_duration_9(self):
        """测试视频过程中扣费--反例"""
        """传入小数时间以及错误的房间号"""
        re = inter.video_duration(0.60, 2360, '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_23_2385')
        self.assertEqual('The seconds must be an integer.', re['message'])

    def test_video_duration_10(self):
        """测试视频过程中扣费--反例"""
        """传入错误的token以及错误的房间号"""
        re = inter.video_duration(60, 2360, 'ABC4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_23_2385')
        self.assertEqual('The selected video unique token is invalid.', re['message'])

    def test_video_duration_11(self):
        """测试视频过程中扣费--反例"""
        """全部参数皆传空"""
        re = inter.video_duration('', '', '', '')
        self.assertEqual('The seconds field is required.', re['message'])

    def test_video_duration_12(self):
        """测试视频过程中扣费--反例"""
        """用户ID传空"""
        re = inter.video_duration('60', '', '4cb4654156c2dea6086fb09f92ff0eaf', 'nene_1609919792833_2360_2385')
        self.assertEqual('decrement success', re['message'])

    def test_video_duration_13(self):
        """测试视频过程中扣费--反例"""
        """token传空"""
        re = inter.video_duration(60, 2360, '', 'nene_1609919792833_2360_2385')
        self.assertEqual('The video unique token field is required.', re['message'])

    def test_video_duration_14(self):
        """测试视频过程中扣费--反例"""
        """用户ID传空，房间ID传空"""
        re = inter.video_duration('60', '', '4cb4654156c2dea6086fb09f92ff0eaf', '')
        self.assertEqual('The channel field is required.', re['message'])

    def test_video_logs(self):
        """测试视频消费/收入记录"""
        re = inter.video_logs()
        self.assertEqual('success', re['message'])

    def test_videoLikes_1(self):
        """测试视频喜欢接口--正例"""
        """均传入正确的参数"""
        re = inter.videoLikes(2360, '42fc91f16d1401efdc7101c34ced770f')
        self.assertEqual('success', re['message'])

    def test_videoLikes_2(self):
        """测试视频喜欢接口--反例"""
        """传入不存在的用户ID"""
        re = inter.videoLikes(60, '42fc91f16d1401efdc7101c34ced770f')
        self.assertEqual('success', re['message'])

    def test_videoLikes_3(self):
        """测试视频喜欢接口--反例"""
        """传入空用户ID"""
        re = inter.videoLikes('', '42fc91f16d1401efdc7101c34ced770f')
        self.assertEqual('The like id field is required.', re['message'])

    def test_videoLikes_4(self):
        """测试视频喜欢接口--反例"""
        """传入错误的token"""
        re = inter.videoLikes(2360, 'ABCD42fc91f16d1401efdc7101c34ced770f')
        self.assertEqual('success', re['message'])

    def test_videoLikes_5(self):
        """测试视频喜欢接口--反例"""
        """传入空token"""
        re = inter.videoLikes(2360, '')
        self.assertEqual('The unique token field is required.', re['message'])

    def test_settle_accounts_1(self):
        """测试精选视频结算接口--正例"""
        """传入正确的参数值"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', 60, 2360)
        self.assertEqual('settle accounts finish', re['message'])

    def test_settle_accounts_2(self):
        """测试精选视频结算接口--反例"""
        """传入错误的房间ID"""
        re = inter.settle_accounts('nene_1609919792833_2360_23', 60, 2360)
        self.assertEqual('The selected channel is invalid.', re['message'])

    def test_settle_accounts_3(self):
        """测试精选视频结算接口--反例"""
        """传入空的房间ID"""
        re = inter.settle_accounts('', 60, 2360)
        self.assertEqual('The channel field is required.', re['message'])

    def test_settle_accounts_4(self):
        """测试精选视频结算接口--反例"""
        """传入正确的房间ID，传入错误0时间"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', 0, 2360)
        self.assertEqual('settle accounts finish', re['message'])

    def test_settle_accounts_5(self):
        """测试精选视频结算接口--反例"""
        """传入正确的房间ID，传入错误小数时间"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', 0.80, 2360)
        self.assertEqual('The duration must be an integer.', re['message'])

    def test_settle_accounts_6(self):
        """测试精选视频结算接口--反例"""
        """传入正确的房间ID，传入空时间"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', '', 2360)
        self.assertEqual('The duration field is required.', re['message'])

    def test_settle_accounts_7(self):
        """测试精选视频结算接口--反例"""
        """传入错误的用户ID"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', 90, 230)
        self.assertEqual('settle accounts finish', re['message'])

    def test_settle_accounts_8(self):
        """测试精选视频结算接口--反例"""
        """传入空的用户ID"""
        re = inter.settle_accounts('nene_1609919792833_2360_2385', 90, '')
        self.assertEqual('The hung up id field is required.', re['message'])

    def tearDown(self):
        print("测试结束")


if __name__ == '__main__':
    unittest.main()
