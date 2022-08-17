import os
from PIL import Image, ImageStat
import csv

# 获取绝对路径
SOURCE_PATH = os.path.realpath(__file__)
SOURCE_DIR = os.path.dirname(SOURCE_PATH)

dir = input('选择分析目录：')

target_dir = SOURCE_DIR + '/result/' + dir + '/'

s_record = [dir]
v_record = [dir]

for file in os.listdir(target_dir):
    img = Image.open(target_dir+file).convert('HSV')
    s_stat = ImageStat.Stat(img.getchannel('S'))
    v_stat = ImageStat.Stat(img.getchannel('V'))
    print(file, '的平均饱和度为（of 255）', s_stat.mean[0], '，平均明度为（of 255）', v_stat.mean[0])
    s_record.append(s_stat.mean[0])
    v_record.append(v_stat.mean[0])

print('全部图片的平均饱和度为（of 255）', sum(s_record[1:])/len(s_record[1:]), '百分比为', sum(s_record[1:])/len(s_record[1:])/2.55)
print('全部图片的平均明度为（of 255）', sum(v_record[1:])/len(v_record[1:]), '百分比为', sum(v_record[1:])/len(v_record[1:])/2.55)

with open('color_ana_s_record.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(s_record)

with open('color_ana_v_record.csv', mode='a', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(v_record)