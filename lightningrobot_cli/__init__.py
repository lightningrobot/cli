# 导入功能
import runbot,install,create

import click
import sys

logo = r"""
      _      _       _     _         _             _____       _           _
     | |    (_)     | |   | |       (_)           |  __ \     | |         | |
     | |     _  __ _| |__ | |_ _ __  _ _ __   __ _| |__) |___ | |__   ___ | |_ 
     | |    | |/ _` | '_ \| __| '_ \| | '_ \ / _` |  _  // _ \| '_ \ / _ \| __|
     | |____| | (_| | | | | |_| | | | | | | | (_| | | \ \ (_) | |_) | (_) | |_ 
     |______|_|\__, |_| |_|\__|_| |_|_|_| |_|\__, |_|  \_\___/|_.__/ \___/ \__|
            __/ |                         __/ |                           
           |___/                         |___/                             
"""

@click.command()
@click.argument('action', type=click.Choice(['run', 'create','version','install']))
@click.argument('type', type=str)
@click.argument('name', type=str)


def main(action, type, name):
    print(logo)
    print("\033[1m⚡闪电机器人⚡\033[0m")
    if action == 'run' :
        runbot.main()
    elif action == 'create':
        create.main()
    elif action == 'version':
        print("1.0.0")
    elif sys.argv[1] == "install":
        if type == 'adapter':
            install.main(1,name)
        elif type == 'plugin': 
            install.main(2,name)
        else :
            print("Invalid action for 'run'. Please use 'build' or 'release'.") 
    elif not action:
        print("未传入参数，请输入 'run' 或 'create'")


if __name__ == "__main__":
    main()