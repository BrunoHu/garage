# coding:utf-8
from itchat.content import *
import os
import logging

import sys   #引用sys模块进来，并不是进行sys的第一次加载
reload(sys)  #重新加载sys
sys.setdefaultencoding('utf8')  ##调用setdefaultencoding函数

path = os.path.abspath('.')

gifs_path = os.path.join(path, "pics")



class SyncMsgs:
    def process(self, msg, msgType):
        if msgType != Text:
            return
