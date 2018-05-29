from PIL import Image
import os
import glob

def changeImg(imgPath):
    img_path = glob.glob(imgPath + "/*.jpg")  
    path_save = imgPath + "/after"  
    for file in img_path:  
        name = os.path.join(path_save, file)  
        im = Image.open(file)  
        im.thumbnail((1920,1280))  
        print(im.format, im.size, im.mode)  
        im.save(name,'JPEG')

if __name__ == '__main__':
    changeImg('D:/www/python-ex')