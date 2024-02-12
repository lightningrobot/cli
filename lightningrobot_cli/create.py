# 导入功能
import install

import requests
import shutil
import zipfile
import os
import pip._internal

def main():
    print("[询问]项目名称")
    name = input()

    # 下载模板文件并解压到指定目录
    template_url = "https://codeload.github.com/LightningRobot/template/zip/refs/heads/main"
    response = requests.get(template_url, stream=True)
    response.status_code == 200
    with open(f"template-main.zip", 'wb') as f:
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
        zip_to_extract = f"template-main.zip"
        unzip_file(zip_to_extract, os.getcwd())
        try:
            os.rename("template-main",name)
            os.unlink("template-main.zip")
        except(FileNotFoundError):
                print("[错误]目录不存在，错误码：404")
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