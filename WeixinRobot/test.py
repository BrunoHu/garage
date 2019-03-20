# coding:utf-8
import itchat
from itchat.content import *
from TuringRobot import TuringRobot
from SaveGifs import SaveGifs
from Doutu import Doutu
from getWords import GetWords
import config

import sys   #引用sys模块进来，并不是进行sys的第一次加载  
reload(sys)  #重新加载sys  
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数


import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

isDebug = True

# plugins = [TuringRobot(), SaveGifs(), Doutu(), GetWords()]
plugins = [GetWords()]


# @itchat.msg_register([MAP, CARD, NOTE, SHARING, FRIENDS, PICTURE, ATTACHMENT])
# def log_msg(msg):
#     printMap(msg)

@itchat.msg_register([TEXT])
def autoReply(msg):
    logging.info(msg)
    for plugin in plugins:
        plugin.process(msg, TEXT)

# @itchat.msg_register(TEXT, isGroupChat=True)
# def text_reply(msg):
#     logging.info("is a group msg")
#     logging.info(msg)

@itchat.msg_register([PICTURE])
def doutu(msg):
    logging.info(msg)
    for plugin in plugins:
        plugin.process(msg, PICTURE)

def updateSelfId():
    users = itchat.get_friends()
    for user in users:
        if user["PYQuanPin"] == u"":
            config.SELF_ID = user["UserName"]
            logging.info("update self userName %s" % config.SELF_ID)


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    updateSelfId()
    itchat.run()