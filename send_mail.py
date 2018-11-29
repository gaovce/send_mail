#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 支持中文邮件
# python sendmail.py 
# 2018/11/29 By gaovce

import smtplib,datetime,sys   #导入SMTP包，时间包和系统包
import os                     #导入OS包
from email.MIMEText import MIMEText #导入邮件文本模块

#date = str(datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S"))

if len(sys.argv) >= 3:  #如果用户输入的参数大于3，那么就提示用户正确的输入格式并且退出程序
   arg1 = sys.argv[1]
   arg2 = sys.argv[2]
   arg3 = sys.argv[3]
  #arg3 = "%s\n[%s]" % ( sys.argv[3],date )
else:
  print "%s example@139.com \"subject\" \"message\"" % (sys.argv[0]) 
  sys.exit(1)

def send_mail(to_list,sub,content):  #定义邮件类
  '''
  to_list: plmm@plmm.com
  sub: xxoo
  content: When Where XXOO
  send_mail("gg@gg.com","sub","content")
  '''
  mail_user = '2975502691@qq.com'
  mail_pass = 'monitor2018';
  mail_host = 'mail.gaovce.com'
  me = str.split(mail_user,"@")[0]+"<"+mail_user+">"
  if isinstance(content,unicode):
    content = str(content)
  #if not isinstance(Subject,unicode):
    Subject = unicode(Subject)
  msg = MIMEText(content,_subtype='plain',_charset='utf-8')  
  msg['Subject'] = Subject
  msg['From'] = me
  msg['To'] = to_list
  msg["Accept-Language"]="zh-CN"
  msg["Accept-Charset"]="ISO-8859-1,utf-8"
  try:
    s = smtplib.SMTP()
    s.connect(mail_host,25)
    s.login(mail_user,mail_pass)
    s.sendmail(me, to_list, msg.as_string())
    s.close()
    return True
  except Exception, e:
    print str(e)
    return False
if __name__ == '__main__':
  if send_mail(arg1,arg2,arg3):
    print "Send Success"
  else:
    print "Send Failed"
