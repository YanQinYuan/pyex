# 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：
# [
# 	[1, 82, 65535],
# 	[20, 90, 13],
# 	[26, 809, 1024]
# ]

#coding=utf-8

#格式化，操作excel
import json
import xlwt
from collections import OrderedDict

file = xlwt.Workbook()  # 创建工作薄
table = file.add_sheet('hungry')  # 创建工作表

file01 = 'num.txt'
with open(file01, 'r', encoding='utf-8') as f:
    data = f.read()
dataList = json.loads(data)  # 字典对象

# 方法一：
# i = 0
# for con in dataList:
#     j = 0
#     for num in con: #循环 list 里面嵌套的 list [1,82,65535]
#         table.write(i,j, num)
#         j += 1
#     i += 1

# 方法二：使用枚举 enumerate

for row,d in enumerate(dataList):
    for col,d2 in enumerate(d):
        table.write(row,col,d2)  
file.save('num.xls')
