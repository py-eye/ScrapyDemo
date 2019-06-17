# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt

class MoviePipeline(object):
    def process_item(self, item, spider):
        # self.output_excel(item)
        with open("E:\\scrapyfiles\\movie\\my_meiju.txt", 'wb') as fp:
            fp.write(item['name'].encode("utf8") + b'\n')

    def output_excel(self, datas):
        # 创建一个Excel文件
        baike = xlwt.Workbook(encoding='utf-8')

        # 创建表单
        sheet1 = baike.add_sheet(u'sheet1', cell_overwrite_ok=True)

        # 设置表格表头
        sheet1.write(0, 0, '电影名', self.set_style('Times New Roman', 220, True))
        # sheet1.write(0, 1, '词条url',self.set_style('Times New Roman',220,True))
        # sheet1.write(0, 2, '摘要',self.set_style('Times New Roman',220,True))
        # 设置表格宽度
        sheet1.col(0).width = (30 * 367)
        # sheet1.col(1).width = (40 * 367)
        # sheet1.col(2).width = (150 * 367)

        # 按i行j列顺序依次存入表格
        for i in range(len(datas)):
            sheet1.write(i + 1, 0, datas[i]['name'])
            # sheet1.write(i+1, 1, self.datas[i]['url'])
            # sheet1.write(i+1, 2, self.datas[i]['summary'])

        # 保存文件
        baike.save('E:\\scrapyfiles\\movie\\meijutop100.xls')

    # 设置单元格样式
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height

        style.font = font

        return style
