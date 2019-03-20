# coding:utf-8
import itchat
from itchat.content import *
from graber import scrabe_with_keyword
import os
import logging
import re
import traceback

path = "/Users/hubingcheng/code/garage/WeixinRobot/words/"

class GetWords:
    def process(self, msg, msgType):
        if msgType != TEXT:
            return
        try:
            text = msg["Text"]
            target = None
            logging.info("get words recieve msg %s" % text)
            target = text.split("帮我找一下")[1].split("的资料吧")[0]
            if target is not None:
                scrabe_with_keyword(target, 10)
                logging.info("get key word %s" % target)
                filename = "%s%s.txt" % (path, target)
                logging.info("file %s exist ? %s " % (filename, os.path.isfile(filename)))
                logging.info("start sending %s" % filename)
                itchat.send(open(filename).read(), msg['FromUserName'])
                logging.info("end sending %s" % filename)
        except Exception, e:
            print traceback.format_exc(e)