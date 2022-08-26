"""实现脚本定时执行"""
import time  # 导入时间包
import os  # 导入系统包
#  start_time = input("请输入用例开始执行到时间，例如12:00")
while True:
    now = time.strftime("%H:%M", time.localtime())  # 获取系统时间
    if now == '18:26':  # 判断获取的时间是否与设定时间相等
        print("开始执行测试用例")
        # 切换到总执行脚本所在到路径
        os.chdir(r'/nene_test/interface_test/execute')
        os.system('python all_execute.py')
        print('测试用例执行结束')
        break  # 跳出循环

    else:
        print("当前系统时间为：%s"%now)
        time.sleep(10)
