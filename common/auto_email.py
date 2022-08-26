import smtplib  # 导入发送核心类
from email.mime.text import MIMEText  # 初始化邮件内容
from email.header import Header  # 初始化邮件头部信息
from email.mime.multipart import MIMEMultipart  # 附件


class auto_email():
    def __init__(self):
        self.mail_host = "smtp.qq.com"  # 配置邮件发送服务，例如qq邮箱
        self.mail_user = '1766353759@qq.com'  # 邮箱发送者账号
        self.mail_password = "xyxdigovtkzwcadh"  # 发送邮箱的授权码
        self.sender = "1766353759@qq.com"  # 与发送者相同
        self.reciver = "v_dreams@digitalgd.com.cn"  # 邮件接受者Jonas.chen@dotcunited.com

    def send_email(self, report):
        # report = "auto_test.html"
        global smote
        with open(report, "rb") as f:
            mail_content = f.read()
        print("debug:",mail_content)
        text_msg = MIMEText(mail_content, 'html', 'utf-8')  # 配置邮件内容
        text_msg['Content_Type'] = 'application/octet-stream'  # 配置邮件类型
        # 创建一个带附件带邮件实例，作为根容器
        main_msg = MIMEMultipart()
        #   将邮件显示内容添加到根容器
        main_msg.attach(text_msg)
        main_msg['From'] = self.sender  # 配置邮件发送方
        main_msg['To'] = self.reciver  # 配置邮件接收方
        main_msg.attach(MIMEText(mail_content, 'html', 'utf-8'))
        text_msg["Content-Disposition"] = 'attachment; filename="API TestReport.html"'  # 附件
        subject = 'Automation report'  # 配置邮件主题
        main_msg['Subject'] = Header(subject, 'utf-8')
        try:
            smote = smtplib.SMTP_SSL(self.mail_host, 465)  # 配置发送端口
            smote.login(self.mail_user, self.mail_password)  # 配置邮箱登陆
            smote.sendmail(self.sender, self.reciver, main_msg.as_string())  #
            smote.quit()
            print('邮件发送成功')

        except smtplib.SMTPException as e:
            print(e)


if __name__ == '__main__':
    ae = auto_email()  # 创建类到对象
    report = r"D:\PythonTest\xiaowen_Python_work\report\API TestReport2021-03-19_19-28-35.html"
    ae.send_email(report)
