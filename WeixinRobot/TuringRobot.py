# coding:utf-8
import itchat
from itchat.content import *
import requests
import config
import json
import logging


import sys   #引用sys模块进来，并不是进行sys的第一次加载  
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

class TuringRobot:
    TURING_API_URL = "http://www.tuling123.com/openapi/api"
    TURING_API_KEY = "c50d6b72df34450a9f82f4f990bd25e1"
    CHAT_INTERVL_IN_SEC =  10 * 60

    def __init__(self):
        self.global_switch_is_open = True     # if false, all user close
        self.user_status = dict()

    def response(self, msg):
        payload = {"key": self.TURING_API_KEY}
        payload["info"] = msg.get("Text", "呵呵")
        payload["userid"] = msg.get("FromUserName", "@default")[1:32]
        rsp = json.loads(requests.post(self.TURING_API_URL, data=payload).text)
        if (rsp.get("code", -1) == 100000):
            return rsp.get("text")
        elif (rsp.get("code", -1) == 40004):
            self.user_status[msg['FromUserName']] = false
            return "今天胡二货血条已空，要躲着微信大魔王了~明天再来找我~想聊天的话可以找胡诚诚本尊哦~"
        return "嘿嘿"

    def process(self, msg, msgType):
        if msgType != TEXT:
            return
        if self.isTrigger(msg["Text"]):
            logging.info("hit trigger %s" % msg["Text"])
            self.check_user_robot_switch(msg)
        elif self.user_status.get(msg['FromUserName'], False):
            if self.global_switch_is_open:
                itchat.send(self.response(msg), msg['FromUserName'])
            else:
                itchat.send(u"胡诚诚1号把我关了，尴尬~", msg['FromUserName'])



    def check_user_robot_switch(self, msg):
        text = msg["Text"]
        if (self.user_status.get(msg['FromUserName'], False) is False and u"陪我聊天" == text):
            logging.info("user %s want talk" % msg['User']['NickName'])
            self.user_status[msg['FromUserName']] = True
            itchat.send(u"现在是胡诚诚2号为你提供聊天服务，本机器人小名胡二货，不要嫌我蠢哦~", msg['FromUserName'])
            itchat.send(u"如果不想和我这二货聊的话可以输入 胡二货拜拜  我会默默离开的", msg['FromUserName'])
        elif u"胡二货拜拜" == text:
            logging.info("user %s want end" % msg['User']['NickName'])
            self.user_status[msg['FromUserName']] = False
            itchat.send(u"有点舍不得，拜~", msg['FromUserName'])
        elif u"关闭图灵" == text and msg['FromUserName'] == config.SELF_ID:
            logging.info("close turing chat bot")
            self.global_switch_is_open = False
        elif u"开启图灵" == text and msg['FromUserName'] == config.SELF_ID:
            logging.info("open turing chat bot")
            self.global_switch_is_open = True
        elif "帮助" == text:
            for text in config.HELP_INFO:
                itchat.send(text, msg['FromUserName'])



    def isTrigger(self, text):
        return text in [u"陪我聊天", u"胡二货拜拜", u"关闭图灵", u"开启图灵", "帮助"]






