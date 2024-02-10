import requests
import shutil
import zipfile
import os
import sys
from pip._internal import main

def get_latest_package_version(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    else:
        print(f"Failed to fetch package info. Status code: {response.status_code}")
        return None

local_version = "0.0.2"

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
    print("[信息]欢迎使用闪电机器人！")
    print("[信息]正在检测更新...")
    # 获取闪电机器人脚手架的最新版本并比较本地版本
    package_name = "lightningrobot"
    latest_version = get_latest_package_version(package_name)
    if latest_version > local_version:
        print("[信息]发现新版本，正在更新...")
        main.main(['install', f'{package_name}=={latest_version}'])
        print("[信息]更新成功！")
    else:
        print("[信息]已是最新版本！")
    print("[信息]正在启动项目...")
    print("[错误]启动失败，机器人未制作完成，请等待正式版。")

# 命令行参数处理
if sys.argv[1] == "create":
    print(logo)
    print("[询问]项目名称")
    name = input()
    # 获取安装目录输入
    print("[询问]安装目录")
    install_path = input()
    os.chdir(install_path)

    # 下载模板文件并解压到指定目录
    template_url = "https://codeload.github.com/LightningRobot/template/zip/refs/heads/main"
    response = requests.get(template_url, stream=True)
    response.status_code == 200
    with open(f"{install_path}/template-main.zip", 'wb') as f:
        shutil.copyfileobj(response.raw, f)

        def unzip_file(zip_path, extract_dir):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_files = zip_ref.namelist()

                for file in zip_files:
                    dest_path = os.path.join(extract_dir, file)

                    if file.endswith('/'):
                        os.makedirs(dest_path)
                    else:
                        parent_dir = os.path.dirname(dest_path)
                        if not os.path.exists(parent_dir):
                            os.makedirs(parent_dir)
                        with open(dest_path, 'wb') as dest_file:
                            dest_file.write(zip_ref.read(file))

        # 解压ZIP文件到指定目录
        zip_to_extract = f"{install_path}/template-main.zip"
        unzip_file(zip_to_extract, install_path)
        try:
            os.rename("template-main",name)
            os.unlink("template-main.zip")
        except(FileNotFoundError):
                print("[错误]目录不存在，错误码：404")
        # 安装适配器包并创建适配器目录
        print("[询问]要使用哪个适配器")
        adaapterfolder = f"lighteningrobot-adapter-" + input()
        adapter = f"lighteningrobot-adapter-" + input()
        main.main(['install', adapter])
        print(f"[信息]成功安装适配器包 {adapter}！（来源：PyPI）")
        path = f"{install_path}/{name}/adapters/{adaapterfolder}"
        os.makedirs(path)
        print("[信息]创建成功！")

if sys.argv[1] == "install":
    print(logo)
    if sys.argv[2] == "adapter":
        adapter = f"lighteningrobot-adapter-" + sys.argv[3]
        main.main(['install', adapter])
        path = f"{install_path}/{name}/adapters/{adapter}"
        os.makedirs(path)
        print(f"[信息]成功安装适配器包 lighteningrobot-adapter-{adapter}！（来源：PyPI）")
    if sys.argv[2] == "plugin":
        plugin = f"lighteningrobot-plugin-" + sys.argv[3]
        main.main(['install', adapter])
        path = f"{install_path}/{name}/adapters/{adapter}"
        os.makedirs(path)
        print(f"[信息]成功安装适配器包 lighteningrobot-adapter-{adapter}！（来源：PyPI）")