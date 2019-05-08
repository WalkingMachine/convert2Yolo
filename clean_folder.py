#-*-coding:utf-8-*-


from os import listdir, remove
from os.path import isfile, join
import re

ImageNetFolder = "/home/jeffrey/Downloads/ImageNet/"
ImageNetObjects = [f for f in listdir(ImageNetFolder)]

#print(ImageNetObjects)

for imageFolder in ImageNetObjects:
    print(imageFolder)
    currentDir = ImageNetFolder+imageFolder
    files = [f for f in listdir(currentDir)]
    
    count = 0
    #zselected_files = filter(str.endswith('.xml'), images)
    
    for i in files:
        if i.endswith('.JPEG'):
            print("true")
            
            if isfile(currentDir+"/"+i[:-4]+"xml"):
                count = count +1
            else:
                remove(currentDir+"/"+i)

    for i in files:
        if i.endswith('.xml'):
            print("true")
            
            if isfile(currentDir+"/"+i[:-3]+"JPEG"):
                count = count +1
            else:
                remove(currentDir+"/"+i)       
    print(count)
      
    #print(selected_files)