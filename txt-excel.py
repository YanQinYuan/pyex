#请将上述内容写到 student.xls 文件中，如下图所示：
#coding=utf-8

#格式化，操作excel
import json
import xlwt3

file = xlwt3.Workbook() #创建工作薄
table = file.add_sheet('test1',cell_overwrite_ok = True)#创建工作表

table.write(1, 0, 'number')
table.write(1, 1, 'name')
table.write(1, 2, 'score')

file = 'student.txt'
with open(file,'r',encoding='utf-8') as f:
    data = f.read()
dataDic = json.loads(data) #字典对象

for i in range(100):
    for listdata in dataDic[1]:
        table.write(i,2,listdata)
