#敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

#coding=utf-8

#思路，先读取到一个列表里，再根据用户输入来逐一匹配

def filterWord(file):
    user_in = input("请输入：")
    with open(file, 'r',encoding='utf-8') as f:
        data = f.read()
    if user_in in data:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    filterWord('D:/www/python-ex/fillterwords.txt')
