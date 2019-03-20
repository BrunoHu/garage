# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import traceback

sender = 'hbc0204@fixmail.com'
receivers = ['526517128@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱



# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
def send(keyword):
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login("17004952990", "hbc02041993")

    path = "%s.txt" % keyword
    message = MIMEMultipart()
    # message['From'] = Header("呆萌的胡诚诚", 'utf-8')
    # message['To'] =  Header("开火车的小雪雯", 'utf-8')

    subject = '%s 的语料' % keyword
    message['Subject'] = Header(subject, 'utf-8')
    text = open(path).read()
    text = "一封邮件一杯咖啡哦~\n************\n\n\n%s" % text
    message.attach(MIMEText(text, 'plain', 'utf-8'))
    # att1 = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
    # att1["Content-Type"] = 'application/octet-stream'
    # att1["Content-Disposition"] = 'attachment; filename="%s"' % keyword
    # message.attach(att1)

    try:
        smtp.sendmail("17004952990@163.com", "hbc0204@foxmail.com", message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException, e:
        print traceback.format_exc(e)
        print "Error: 无法发送邮件"

if __name__ == "__main__":
    send("文脈")
