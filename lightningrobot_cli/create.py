# 导入所需模块
from lightningrobot_cli import install
import requests
import zipfile
import os
import pip._internal

def main():
    # 询问项目名称并获取用户输入
    print("[询问]项目名称")
    name = input()

    # 定义 GitHub 模板仓库的 URL
    url = 'https://codeload.github.com/LightningRobot/template/zip/refs/heads/main'
    # 下载压缩包到本地
    template = requests.get(url)
    with open('template.zip', 'wb') as f:
        f.write(template.content)
    # 解压下载的 ZIP 文件
    with zipfile.ZipFile('template.zip') as zip_file:
        zip_file.extractall()
    # 修改解压后的目录名称为用户提供的项目名称
    os.rename("template-main", name)

    # 删除 ZIP 文件
    os.remove('template.zip')
    # 打印创建成功消息
    print("[信息]创建基本项目成功！")
    
    # 提示用户选择适配器并获取输入
    print("[询问]要使用哪个适配器")
    adaptername = input()
    adapter_package = f"lightningrobot-adapter-{adaptername}"
    # 使用 pip 安装指定适配器
    pip._internal.main(['install', adapter_package])
    # 打印安装成功消息
    print(f"[信息]成功安装适配器包 {adapter_package}！（来源：PyPI）")
    # 打印创建路径成功的消息
    print("[信息]创建成功！")    

if __name__ == "__main__":
    main()