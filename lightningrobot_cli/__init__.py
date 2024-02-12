# 导入功能
import runbot
import install
import create

import sys
from pip._internal import main

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

if sys.argv[1] == "run":
    print(logo)
    runbot.main()
if sys.argv[1] == "create":
    print(logo)
    create.main()
if sys.argv[1] == "install":
    print(logo)
    name = sys.argv[3]
    if sys.argv[2] == "adapter":
        install.main(1,name)
    if sys.argv[2] == "plugin":
        install.main(2,name)