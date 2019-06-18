# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt

class MoviePipeline(object):

    def __init__(self):
        self.num = 0

        # 创建一个Excel文件
        self.meiju_info = xlwt.Workbook(encoding='utf-8')

        # 创建表单
        self.sheet1 = self.meiju_info.add_sheet(u'sheet1', cell_overwrite_ok=True)

        # 设置表格表头
        self.sheet1.write(0, 0, '电影名', self.set_style('Times New Roman', 220, True))
        self.sheet1.write(0, 1, '状态', self.set_style('Times New Roman', 220, True))
        self.sheet1.write(0, 2, '小分类', self.set_style('Times New Roman', 220, True))
        self.sheet1.write(0, 3, '电视台', self.set_style('Times New Roman', 220, True))
        self.sheet1.write(0, 4, '更新日期', self.set_style('Times New Roman', 220, True))

        # 设置表格宽度
        self.sheet1.col(0).width = (27 * 367)
        self.sheet1.col(1).width = (12 * 367)
        self.sheet1.col(2).width = (27 * 367)
        self.sheet1.col(3).width = (13 * 367)
        self.sheet1.col(4).width = (13 * 367)


    def process_item(self, item, spider):
        self.sheet1.write(self.num + 1, 0, item['name'])
        self.sheet1.write(self.num + 1, 1, item['statu'])
        self.sheet1.write(self.num + 1, 2, item['stype'])
        self.sheet1.write(self.num + 1, 3, item['tv'])
        self.sheet1.write(self.num + 1, 4, item['update_time'])

        self.num+=1

        # 保存到Excel文件
        self.meiju_info.save('E:\\scrapyfiles\\movie\\meijutop100.xls')


    # 设置单元格样式
    def set_style(self, name, height, bold=False):
        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 5
        font.height = height

        style = xlwt.XFStyle()  # 初始化样式
        style.num_format_str = 'MM/DD/YYYY'
        style.font = font

        return style
