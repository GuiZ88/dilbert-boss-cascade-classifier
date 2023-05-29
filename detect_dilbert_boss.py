import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
  
# declare the classifiers for dilbert and boss
dilbert_cascade = cv2.CascadeClassifier('dilbert/data/cascade.xml')
dogbert_cascade = cv2.CascadeClassifier('ponty-haired-boss/data/cascade.xml')

def detect_dilbert_dogbert(img):     

    dogbert_find = False
    dilbert_find = False

    dilbert_img = img.copy()   
    dilbert_rect = dilbert_cascade.detectMultiScale(dilbert_img,
                                            scaleFactor = 1.2,
                                            minNeighbors = 10)   
    dogbert_rect = dogbert_cascade.detectMultiScale(dilbert_img,
                                            scaleFactor = 1.2,
                                            minNeighbors = 10)       
  
    dilbert_midpoint = []
    for (x, y, w, h) in dilbert_rect:
        cv2.rectangle(dilbert_img, (x, y),
                      (x + w, y + h), (0, 0, 255), 2) 
        dilbert_find = True      
        dilbert_midpoint = ((x+(x+w))/2, (y+(y+h))/2)
        
    dogbert_midpoint = []
    for (x, y, w, h) in dogbert_rect:
        cv2.rectangle(dilbert_img, (x, y),
                      (x + w, y + h), (0, 255, 0), 2)      
        dogbert_find = True
        dogbert_midpoint = ((x+(x+w))/2, (y+(y+h))/2)
       
    if dogbert_find and dilbert_find: 
        return (dilbert_img, dilbert_midpoint, dogbert_midpoint)
    else: return None
        
 

directory = "undefined/"
hs = open("detect_dilbert_boss.txt","a")
for filename in os.listdir(directory):

    f_read = os.path.join(directory, filename)
    f_write = os.path.join("detected/", filename)
    img = cv2.imread(f_read)
    result = detect_dilbert_dogbert(img)

    try:
        if result != None:    
            if len(result) == 3:
                line = "{0} {1} {2} {3} {4}\n"
                line = line.format(filename, result[1][0], result[1][1], result[2][0], result[2][1])
                print(filename)
                print(line)
                cv2.imwrite(f_write, result[0])
                hs.write(line)
    except:
        hs.write(filename + " 0 0\n") 
        print("exception")

hs.close()