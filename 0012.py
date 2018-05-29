# 敏感词文本文件 filtered_words.txt，
# 里面的内容 和 0011题一样，当用户输入敏感词语，
# 则用 星号 * 替换，例如当用户输入「北京是个好城市」，
# 则变成「**是个好城市」。


#思路：用结巴分词把输入内容拆分开，匹配，再输出。
#coding=utf-8
import jieba

def filterW(words):
    seg_list = jieba.cut(words, cut_all=False)
    data = " ".join(seg_list)
    listd = data.split() # 变成list
    file = 'D:/www/python-ex/fillterwords.txt'
    with open(file, 'r', encoding='utf-8') as f:
        fliter_data = f.read()
    # print(data)
    a = 0
    for i in listd:
        if i in fliter_data:
            i = "*"
            listd[a] = i
            a += 1
        else:
            a += 1
    print(''.join(listd))


if __name__ == '__main__':
    user_w = input("请输入：")
    filterW(user_w)

