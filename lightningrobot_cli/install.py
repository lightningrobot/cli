import requests
import os
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
    
def get_package_config(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data['home_page']
    else:
        print(f"Failed to fetch package info. Status code: {response.status_code}")
        return None
    
def main(conmand,name):
    if conmand == 1:
        adapter = f"lighteningrobot-adapter-" + name
        main.main(['install', adapter])
        path = f"adapters/{adapter}"
        os.makedirs(path)
        adapter_url = get_package_config(adapter)
        print(f"[信息]成功安装适配器包 {adapter}！（来源：PyPI）")
    if conmand == 2:
        plugin = f"lighteningrobot-plugin-" + name
        main.main(['install', plugin])
        path = f"plugins/{plugin}"
        os.makedirs(path)
        print(f"[信息]成功安装插件 {name}！（来源：PyPI）")