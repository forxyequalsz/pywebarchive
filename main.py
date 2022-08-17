#!/usr/bin/env python3

import os
import shutil
import sys
import webarchive
import tempfile
import textwrap
import time
from PIL import Image

# 获取绝对路径
SOURCE_PATH = os.path.realpath(__file__)
SOURCE_DIR = os.path.dirname(SOURCE_PATH)
SOURCE_PARENT = os.path.dirname(SOURCE_DIR)

# Import our local copy of the webarchive module
sys.path.insert(0, SOURCE_PARENT)

# Directory containing sample data
# SAMPLE_DATA_DIR = os.path.join(SOURCE_PARENT, "pywebarchive", "sample_data")
SAMPLE_DATA_DIR = "/Users/zhangxiaoyu/Documents/摄影相关/摄影画集"

ip = input("请输入webarchive文件名：")
if ip.endswith('.webarchive'):
    file_name = ip
else:
    file_name = ip + ".webarchive"

position = file_name.find('CNU')-3
result_file_name = file_name[0:position]
result_dir = SOURCE_DIR + '/result/' + result_file_name

# Path to our sample archive
SAMPLE_ARCHIVE_PATH = os.path.join(SAMPLE_DATA_DIR, file_name)

def run_unzip():
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_path = os.path.join(tmp_dir, result_file_name+".html")
        assert (not os.path.exists(output_path))

        # 读取并解包webarchive
        with webarchive.open(SAMPLE_ARCHIVE_PATH) as archive:
            # Extract the archive, and assert that it succeeded
            archive.extract(output_path)
            assert os.path.isfile(output_path)
            output_pic_dir = os.path.join(tmp_dir, result_file_name + "_files")
            # 创建同名结果目录
            os.mkdir(result_dir)

            # 判断文件类型
            for file in os.listdir(output_pic_dir):
                if file.endswith('.jpg') or file.endswith('.png'):
                    pic_path = os.path.join(output_pic_dir, file)
                    img = Image.open(pic_path).size
                    # 判断图片尺寸
                    if img[0] > 399 and img[1] > 399:
                        print(file)
                        # 把符合条件的移动到结果目录
                        shutil.move(pic_path, result_dir)

        # 提示完成
        print(textwrap.dedent("""\
            Extracted Done.."""))


if __name__ == "__main__":
    run_unzip()
    # 等几秒
    time.sleep(3)
