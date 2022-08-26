"""用户相关的配置"""
import os

#  项目地址
url = ''

#  访问项目的账号
username = '1766353759@qq.com'
password = 123456789

#  项目路径
print(os.path.abspath(__file__))
# dirname 获取脚本所在的文件夹
print(os.path.dirname(os.path.abspath(__file__)))
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#  截图路径
img_path = project_path + '\\img\\'
print(img_path)

#  报告路径
report_path = project_path + '\\report\\'
print(report_path)

#  用例所在的路径
case_path = project_path + '\\testcase\\'
print(case_path)

#  日志所在的路径
log_path = project_path + '\\log\\'
print(log_path)