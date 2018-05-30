#请将上述内容写到 student.xls 文件中，如下图所示：
#coding=utf-8

#格式化，操作excel
import json
import xlwt
from collections import OrderedDict

file = xlwt.Workbook() #创建工作薄
table = file.add_sheet('test1')  # 创建工作表

file01 = 'student.txt'
with open(file01,'r',encoding='utf-8') as f:
    data = f.read()
dataDic = json.loads(data) #字典对象

# n = 1
# for i in range(1,100):
#     if i in dataDic:
#         print("asdf" + dataDic.get(i))
#         for listdata in dataDic.get(i):
#             print(listdata)
#             table.write(i,n,listdata)
#             n +=1
#     else:
#         print('end')
#         pass

i = 0
for con in dataDic:
    values = dataDic.get(con)
    table.write(i, 0, con)
    j = 1
    for value in values:
        table.write(i, j, value)
        j += 1
    i += 1

file.save('student_excel.xls')
