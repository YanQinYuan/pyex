#coding = utf-8
import os
import glob
from collections import Counter
from countWord import getData

def countTxt(txtPath):
    txt_path = glob.glob(txtPath + "/*.txt") 
    # path_save = txtPath + "/after"  
    for file in txt_path:  
        data = getData(file)
        c = Counter(data)
        res = c.most_common()[:1]
        print("file:" + file + "word:" + res[0][0] + 'count:' + str(res[0][-1]))
        
        

if __name__ == '__main__':
    countTxt("D:/www/python-ex")
