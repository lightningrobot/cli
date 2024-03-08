import time
import os
import lightningrobot

# 定义常量
WELCOME_PREFIX = '[欢迎]'
PLUGIN_DIR = 'plugins'

def check_time():
    mytime = time.localtime()
    if 8 <= mytime.tm_hour < 12:
        return 'morning'
    elif 12 <= mytime.tm_hour < 18:
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

def main():
    time = check_time()
    print_greeting(time)
    try:
        if not os.path.exists(PLUGIN_DIR):
            print("[错误]当前目录不是一个闪电机器人项目，请检查！")
            raise SystemExit(0)
    except Exception as e:
        lightningrobot.log.error(f"检查插件目录时出现异常：{e}")
        raise SystemExit(0)
    
    print("[信息]正在启动项目...")
    lightningrobot.start()

if __name__ == "__main__":
    main()