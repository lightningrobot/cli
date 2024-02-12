# 导入功能
import lighteningrobot

import os
import time
import sys
from pip._internal import main

def hello():
    mytime = time.localtime()
    if mytime.tm_hour < 8:
     print('[欢迎]早上好！元气满满的一天开始啦！')
    elif mytime.tm_hour < 12 >8:
        print('[欢迎]上午好！今天看起来精神不错呢！')
    elif mytime.tm_hour < 18 > 12:
        print('[欢迎]不必行色匆匆，不必光芒四射，不必成为别人，只需做自己。下午好。')
    else:
        print('[欢迎]快乐的一天又结束了！晚上好！')

def main():
    print("[信息]欢迎使用闪电机器人！")
    filename = sys.argv[0]
    runname = filename[-2:]
    if runname == "py":
        print("[警告]您当前正在使用开发版脚手架，有任何问题请及时在Github上报。")
        status = "Dev"
    else:
        hello()
        status = "Normal"
    if not os.path.exists("plugins"):
        print("[错误]当前目录不是一个闪电机器人项目，请检查！")
        raise SystemExit(0)
    print("[信息]正在启动项目...")
    if status == "Dev":
            lighteningrobot.dev()
    if status == "Normal":
            lighteningrobot.start()