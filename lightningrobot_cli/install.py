import requests
import pip._internal
from lightningrobot import log

# 添加一个通用的函数来处理 HTTP 请求
async def fetch_json(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 若状态码非 200，则抛出异常
        return response.json()
    except requests.RequestException as e:
        await log.error(f"请求错误: {e}")
        return None

async def get_latest_package_version(package_name):
    url = f'https://pypi.org/pypi/{package_name}/json'
    data = await fetch_json(url)
    if data:
        return data['info'].get('version')
    else:
        return None
    
async def main(command, name):
    if command == 1:
        adapter = f"lightningrobot-adapter-{name}"
        pip._internal.main(['install', adapter])
        await log.info(f"成功安装适配器包 {adapter}！（来源：PyPI）")
    elif command == 2:
        plugin = f"lightningrobot-plugin-{name}"
        pip._internal.main(['install', plugin])
        path = f"plugins/{plugin}"
        await log.info(f"成功安装插件 {plugin}！（来源：PyPI）")