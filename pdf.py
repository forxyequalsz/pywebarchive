import os, shutil
from reportlab.pdfbase import pdfmetrics   # 注册字体
from reportlab.pdfbase.ttfonts import TTFont # 字体类
# 注册字体
pdfmetrics.registerFont(TTFont('Alibaba-PuHuiTi-Bold', 'Alibaba-PuHuiTi-Bold.ttf'))

from reportlab.platypus import Table, SimpleDocTemplate, Paragraph, Image  # 报告内容相关类
from reportlab.lib.pagesizes import A4  # 页面的标志尺寸(8.5*inch, 11*inch)
from reportlab.lib.styles import getSampleStyleSheet  # 文本样式
from reportlab.lib import colors  # 颜色模块
from reportlab.lib.units import cm  # 单位：cm
from reportlab.platypus import PageBreak


class Graphs:
    # 绘制标题
    @staticmethod
    def draw_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Heading1']
        # 单独设置样式相关属性
        ct.fontName = 'Alibaba-PuHuiTi-Bold'  # 字体名
        ct.fontSize = 64  # 字体大小
        ct.leading = 50  # 行间距
        ct.textColor = colors.black  # 字体颜色
        ct.alignment = 1  # 居中
        ct.bold = True
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制小标题
    @staticmethod
    def draw_little_title(title: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 拿到标题样式
        ct = style['Normal']
        # 单独设置样式相关属性
        ct.fontName = 'SimSun'  # 字体名
        ct.fontSize = 15  # 字体大小
        ct.leading = 30  # 行间距
        ct.textColor = colors.red  # 字体颜色
        # 创建标题对应的段落，并且返回
        return Paragraph(title, ct)

    # 绘制普通段落内容
    @staticmethod
    def draw_text(text: str):
        # 获取所有样式表
        style = getSampleStyleSheet()
        # 获取普通样式
        ct = style['Normal']
        ct.fontName = 'SimSun'
        ct.fontSize = 12
        ct.wordWrap = 'CJK'  # 设置自动换行
        ct.alignment = 0  # 左对齐
        ct.firstLineIndent = 32  # 第一行开头空格
        ct.leading = 25
        return Paragraph(text, ct)

    # 绘制图片
    @staticmethod
    def draw_img(path):
        img = Image(path)  # 读取指定路径下的图片
        Width = img.imageWidth
        Height = img.imageHeight
        img.drawWidth = Width / 72 * cm  # 设置图片的宽度
        img.drawHeight = Height / 72 * cm  # 设置图片的高度
        return img

if __name__ == '__main__':
    # 创建内容对应的空列表
    content = list()

    # 添加标题
    content.append(Graphs.draw_title('测试名称'))
    content.append(PageBreak())

    # 添加图片
    content.append(Graphs.draw_img('/Users/zhangxiaoyu/PycharmProjects/pywebarchive/result/艳丽的色彩，荒诞的日常 | 摄影大师Martin Parr/3ec27180af683266b370eff39c978e30.jpg'))

    # 生成pdf文件
    doc = SimpleDocTemplate('report.pdf', pagesize=A4)
    doc.build(content)