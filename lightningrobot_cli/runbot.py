import time
from lightningrobot import log
import sys

# 定义常量
WELCOME_PREFIX = '[欢迎-Welcome]'

def check_time():
    thetime = time.localtime()
    if 8 <= thetime.tm_hour < 12:
        return 'morning'
    elif 12 <= thetime.tm_hour < 18:
        return 'afternoon'
    else:
        return 'evening'

def print_greeting(time_of_day):
    if time_of_day == 'morning':
        print(WELCOME_PREFIX + '早上好！元气满满的一天开始啦！')
    elif time_of_day == 'afternoon':
        print(WELCOME_PREFIX + '下午好。不必行色匆匆，不必光芒四射，不必成为别人，只需做自己。')
    else:
        print(WELCOME_PREFIX + '快乐的一天又结束了！晚上好！')