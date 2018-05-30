# 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
# { "1" : "上海", "2" : "北京", "3" : "成都"}

#coding=utf-8

#格式化，操作excel
import json
import xlwt
from collections import OrderedDict

file = xlwt.Workbook()  # 创建工作薄
table = file.add_sheet('hungry')  # 创建工作表

file01 = 'city.txt'
with open(file01, 'r', encoding='utf-8') as f:
    data = f.read()
dataDic = json.loads(data)  # 字典对象

i = 0
j = 0
for con in dataDic:
    values = dataDic.get(con)
    table.write(i, 0, con)
    table.write(i,1,values)
    i +=1
file.save('city.xls')
