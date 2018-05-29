#coding = utf-8
import os
import glob
from collections import Counter

import jieba


def getData(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
    return data

def countTxt(txtPath):
    txt_path = glob.glob(txtPath + "/*CN.txt") 
    # path_save = txtPath + "/after"  
    for file in txt_path:  
        data = getData(file)
        seg_list = jieba.cut(data, cut_all=True, HMM=False)
        Adata = " ".join(seg_list)
        c = Counter(Adata)
        res = c.most_common()[:1]
        print(res)
        print("file:" + file + "     word:" + res[0][0] + 'count:' + str(res[0][-1]))

        

if __name__ == '__main__':
    countTxt("D:/www/python-ex")
