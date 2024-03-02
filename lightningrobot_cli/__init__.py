# 导入功能
from . import runbot,install,create

import sys

logo = """\
      _      _       _     _         _             _____       _           _
     | |    (_)     | |   | |       (_)           |  __ \     | |         | |
     | |     _  __ _| |__ | |_ _ __  _ _ __   __ _| |__) |___ | |__   ___ | |_ 
     | |    | |/ _` | '_ \| __| '_ \| | '_ \ / _` |  _  // _ \| '_ \ / _ \| __|
     | |____| | (_| | | | | |_| | | | | | | | (_| | | \ \ (_) | |_) | (_) | |_ 
     |______|_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |_|  \_\___/|_.__/ \___/ \__|
            __/ |                         __/ |                           
           |___/                         |___/                             
"""


def main():
    print(logo)
    print("\033[1m⚡闪电机器人⚡\033[0m")
    if sys.argv[1] == "run":
        runbot.main()
    if sys.argv[1] == "create":
        create.main()
    if sys.argv[1] == "version":
        print("0.1.6")
    if sys.argv[1] == "install":
        name = sys.argv[3]
        if sys.argv[2] == "adapter":
            install.main(1,name)
        if sys.argv[2] == "plugin":
            install.main(2,name)

if __name__ == "__main__":
    main()