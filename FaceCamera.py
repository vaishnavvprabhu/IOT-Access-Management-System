#Contingency Code
# def camera(name):
#     from picamera import PiCamera
#     import time
#     
#     camera = PiCamera()
#     time.sleep(2)
# 
#     camera.capture("/home/pi/HawkEye-main/%s.jpg"%(name))
#     print("Done.")
# 
# # name=input("name : ")
# # camera(name)

#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

# import cv2 #For Image processing 
# import numpy as np #For converting Images to Numerical array 
# import os #To handle directories 
# from PIL import Image #Pillow lib for handling images 
# def camera(people_name):
#     # labels = ["Vaishnav", "Elon Musk"]
#     labels = ["Vaishnav"] 
#     
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     recognizer = cv2.face.LBPHFaceRecognizer_create()
#     recognizer.read("face-trainner.yml")
# 
#     cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera
# 
# 
# 
#     while(True):
# 
#         ret, img = cap.read() # Break video into frames
#         img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
#         img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# #         gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
# #         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
# #         for (x, y, w, h) in faces:
# #             roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 
# # 
# #             id_, conf = recognizer.predict(roi_gray) #recognize the Face
# #         
# #             if conf>=80:
# #                 
# #                 font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name
# #                 name = labels[id_] #Get the name from the List using ID number
# #                 cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
# #                 break
# #                 cv2.imwrite(f'/home/img/{people_name}.png',img)
# #                 break
# #             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# #             
# # 
# #         cv2.imshow('Preview',img) #Display the Video
# #         if cv2.waitKey(20) & 0xFF == ord('q'):
# #             break
#     
# 
#     # When everything done, release the capture
#     cap.release()
#     cv2.destroyAllWindows()


#Contigency plan-2
from picamera import PiCamera
import time


def cameraPi(name):
    camera = PiCamera()
    camera.start_preview()
    camera.start_recording('%s.h264'%(name))
    time.sleep(10)
    camera.stop_recording()
    camera.stop_preview()
cameraPi("Vaihnav")
