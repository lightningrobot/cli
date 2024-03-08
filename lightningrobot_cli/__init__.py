import click
from lightningrobot_cli import create, install, runbot
from lightningrobot import log

# 项目标识符
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

@click.group()
def main():
    """
    主程序入口。
    """
    pass

@main.command('run')
def run_command():
    """
    运行机器人命令。
    """
    print(logo)
    print("\033[1m⚡闪电机器人⚡\033[0m")
    runbot.main()

@main.command('create')
def create_command():
    """
    创建新机器人项目命令。
    """
    print(logo)
    print("\033[1m⚡闪电机器人⚡\033[0m")
    create.main()

@main.command('version')
def version_command():
    """
    显示当前版本信息。
    """
    print(logo)
    print("0.1.8")

@main.command('install')
@click.argument('install_type', type=click.Choice(['adapter', 'plugin'], case_sensitive=False), required=True)
@click.argument('name', type=str, required=True)
def install_command(install_type, name):
    """
    安装适配器或插件命令。

    :param install_type: 安装类型，可选 'adapter' 或 'plugin'。
    :param name: 要安装的适配器或插件的名称。
    """
    print(logo)
    print("\033[1m⚡闪电机器人⚡\033[0m")
    if install_type == "adapter":
        install.main(1, name)
    elif install_type == "plugin":
        install.main(2, name)
    else:
        log.error("选择的安装类型无效。请使用'adapter'或'plugin'。")

if __name__ == "__main__":
    main()