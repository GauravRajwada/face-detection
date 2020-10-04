# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:39:05 2020

@author: Gaurav
"""

import cv2
import numpy as np

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_extractor(img):
    
    faces=face_classifier.detectMultiScale(img,1.3,5)
    if faces is ():
        return None
    
    for (x,y,w,h) in faces:
        x=x-10
        y=y-10
        cropped_face=img[y:y+h+50,x:x+w+50]
        
    return cropped_face

cap=cv2.VideoCapture(0)
count=0

while True:
    ret,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face=cv2.resize(face_extractor(frame),(400,400))
        
        #For training
        if count <300:
            path='E:/Python Project/Face Detection/Dataset/Training/Tanu/'+"train"+str(count)+'.jpeg'
            cv2.imwrite(path,face)
        #For testing
        else:
            path='E:/Python Project/Face Detection/Dataset/Testing/Tanu/'+"test"+str(count)+'.jpeg'
            cv2.imwrite(path,face)
            
        
        #Display count on webcam
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    
    else:
        print("Face not found")
    
    # 13 is for enter key
    if cv2.waitKey(1)==13 or count==400:
        break

cap.release()
cv2.destroyAllWindows()
print('Collecting Sample Complete')
                
        
        
