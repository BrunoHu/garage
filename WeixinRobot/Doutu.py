# coding:utf-8
import itchat
from itchat.content import *
import os
import random
import logging
import config

import sys   #引用sys模块进来，并不是进行sys的第一次加载 
reload(sys)  #重新加载sys 
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

path = os.path.abspath('.')

gifs_path = os.path.join(path, "pics")

class Doutu:
    def __init__(self):
        self.status = True

    def process(self, msg, msgType):
        logging.info("now doutu process %s" % msgType)
        if msgType == PICTURE and self.status:
            random_gif = os.path.join(gifs_path, random.choice(os.listdir(gifs_path)))
            logging.info("selected pic is %s" % random_gif)
            result = itchat.send('@%s@%s' % ('img', random_gif), msg['FromUserName'])
            logging.info("selected pic is %s and send %s" % (random_gif, result))
        elif msgType == TEXT and msg['FromUserName'] == config.SELF_ID:
            if "开启斗图" == msg["Text"]:
                logging.info("open doutu mode")
                self.status = True
            elif "关闭斗图" == msg["Text"]:
                logging.info("close doutu mode")
                self.status = False
        else:
            return


