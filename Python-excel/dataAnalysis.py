# coding:utf-8
# 导入读取Excel的库
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 导入需要读取Excel表格的路径

data = pd.read_excel('/Users/judezeng/Desktop/111.xls', sheet_name='销售明细')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 使图形能够正常显示中文

print(data.tail(2))






