# coding:utf-8
# 导入读取Excel的库
import xlrd
import pandas as pd
import matplotlib.pyplot as plt

# 导入需要读取Excel表格的路径
data = xlrd.open_workbook(r'/Users/judezeng/Desktop/111.xls')

# 计算行、列
print(data.sheet_by_index(0).nrows)
print(data.sheet_by_index(0).ncols)


