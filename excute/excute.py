"""生成自动化测试报告"""

import HTMLTestRunner  # 导入生成HTML的测试报告
import time  # 导入时间包
import unittest  # 导入单元测试框架
from xiaowen_Python_work.common.auto_email import auto_email  # 导入发送邮件的类

# 定义测试用例所在的路径
case_test = r'D:\xiaowen_Python_work\testcase\testcase.py\\'
# 自动发现的方式，来加载目录中所有以testcase开头的脚本
test_dir = '../testcase'
suit = unittest.defaultTestLoader.discover(test_dir, pattern='testcase.py')

report_path = r'D:\xiaowen_Python_work\report\\'
# 测试报告的文件名
# 获取系统时间并转换为字符串格式
now = time.strftime("20%y-%m-%d_%H-%M-%S", time.localtime())
report_name = report_path + "API TestReport" + now + ".html"
# 使用写入的方式打开定义好的报告文件，会新建一个空白报告
Ne = open(report_name, "wb")  # wb 以二进制的方式写入

# 使用可以生成报个的执行器
runner = HTMLTestRunner.HTMLTestRunner(
    # 会将测试过程中的数据写入到Ne中
    stream=Ne, tester="李晓文", title="自动化测试报告"
)

runner.run(suit)
Ne.close()  # 关闭打开的文件

ae = auto_email()  # 创建对象
ae.send_email(report_name)  # 将报告作为邮件内容发送
# report_name   就是这次执行生成的报告名


