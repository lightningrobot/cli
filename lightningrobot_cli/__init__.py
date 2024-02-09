import sys
import requests
from xml.etree.ElementTree import fromstring

def get_latest_package_version(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['info']['version']
    else:
        print(f"Failed to fetch package info. Status code: {response.status_code}")
        return None

# 使用方法
package_name = "lightningrobot"
latest_version = get_latest_package_version(package_name)
if latest_version is not None:
    print(f"欢迎使用 闪电机器人-脚本架\n当前版本：v0.0.1\n最新版本：{latest_version}")
    if latest_version != "0.0.1":
        print("[error]请更新脚本架！")
    else:
        print("[info]脚本架已是最新版本！")

if len(sys.argv) > 1 and sys.argv[1] == "start":
    print("正在启动机器人...")
if len(sys.argv) > 1 and sys.argv[1] == "create":
    print("正在创建机器人...")