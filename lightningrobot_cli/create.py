# 导入功能
from . import install

import requests
import zipfile
import os
import pip._internal

def main():
    print("[询问]项目名称")
    name = input()
    url = 'https://codeload.github.com/LightningRobot/template/zip/refs/heads/main'
    botfile = requests.get(url)
    open('bot.zip', 'wb').write(botfile.content)
    zip_file = zipfile.ZipFile('bot.zip')
    # 解压
    zip_file.extractall()
    os.rename("template-main",name)
    # 安装适配器包并创建适配器目录
    print("[询问]要使用哪个适配器")
    adaptername = input()
    adapter = f"lighteningrobot-adapter-" + adaptername
    pip._internal.main(['install', adapter])
    adapter_url = install.get_package_config(adapter)
    print(f"[信息]成功安装适配器包 {adapter}！（来源：PyPI）")
    path = f"{name}/adapters/{adaptername}"
    os.makedirs(path)
    print("[信息]创建成功！")