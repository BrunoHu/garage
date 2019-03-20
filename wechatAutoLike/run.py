# coding: utf-8
#!/usr/bin/python


from PIL import Image
import numpy as np
import os
import sys
import time




menu_pattern = np.load("menu_pattern.npy")
like_pattern = np.load("like_pattern.npy")

def find(img):
    
    l = len(menu_pattern)
    ll = len(menu_pattern[0])
    imgData = np.array(img)
    for i in xrange(len(imgData) / 4 * 3 ):
        if (imgData[i:i+l,977:977+ll] == menu_pattern).all():
            if (imgData[i+100:i+150, 200:250] == like_pattern).all():
                print "line %s liked, skip" % i
            else:
                return 990, i
    return -1, -1

def like(button):
    if button[1] == -1:
        print "skip"
        return
    os.system("adb shell input tap %s %s" % button)
    time.sleep(0.5)
    likeButton = (button[0]-550, button[1])
    print "like button %s %s " % likeButton
    os.system("adb shell input tap %s %s" % likeButton)
    time.sleep(0.5)


def run():
    os.system("adb shell screencap -p /sdcard/snap.png")
    time.sleep(0.5)
    os.system("adb pull  /sdcard/snap.png")
    time.sleep(0.5)
    grey = Image.open("snap.png").convert('L')
    button = find(grey)
    print "button %s %s " % button
    like(button)
    os.system("adb shell input swipe 100 800  100 200")
    time.sleep(2)



if __name__ == "__main__":
    count = int(sys.argv[1])
    for i in range(count):
        run()