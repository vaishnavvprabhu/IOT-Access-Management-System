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

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images
import time
def camera(people_name):
    # labels = ["Vaishnav", "Elon Musk"]
    labels = ["Vaishnav"] 
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("face-trainner.yml")

    cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera
    # # Define the duration (in seconds) of the video capture here
    capture_duration = 10
 
            
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('%s.avi'%(people_name),fourcc, 20.0, (640,480))
            
    start_time = time.time()
    while( int(time.time() - start_time) < capture_duration ):
        ret, frame = cap.read() # Break video into frames
        if ret==True:
            
#             frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
#             frame = cv2.rotate(frame, cv2.cv2.ROTATE_90_CLOCKWISE)
            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 
    # 
                id_, conf = recognizer.predict(roi_gray) #recognize the Face
    #         
    #             if conf>=80:
    # #                 
    # #                 font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name
    # #                 name = labels[id_] #Get the name from the List using ID number
    # #                 cv2.putText(img, name, (x,y), font, 1, (0,0,255), 2)
    # #                 break
    # #                 cv2.imwrite(f'/home/img/{people_name}.png',img)
    # #                 break
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            frame = cv2.flip(frame,0)
             
            # write the flipped frame
            out.write(frame)
             
            cv2.imshow('frame',frame)
             #if cv2.waitKey(1) & 0xFF == ord('q'):
             #    break
            #print("Capturing the video")
        else:
            break
                
                
                        

        #cv2.imshow('Preview',img) #Display the Video
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
#camera("Vaishnav")

# 
# #Contigency plan-2
# from picamera import PiCamera
# import time
# 
# 
# def cameraPi(name):
#     camera = PiCamera()
#     camera.start_preview()
#     camera.start_recording('%s.h264'%(name))
#     time.sleep(10)
#     camera.stop_recording()
#     camera.stop_preview()
# cameraPi("Vaihnav")


#OpenCV code for video capture

# import numpy as np
# import cv2
# import time
# 
# # Define the duration (in seconds) of the video capture here
# capture_duration = 10
# 
# cap = cv2.VideoCapture(0)
# 
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
# 
# start_time = time.time()
# while( int(time.time() - start_time) < capture_duration ):
#     ret, frame = cap.read()
#     if ret==True:
#         frame = cv2.flip(frame,0)
# 
#         # write the flipped frame
#         out.write(frame)
# 
#         cv2.imshow('frame',frame)
#         #if cv2.waitKey(1) & 0xFF == ord('q'):
#         #    break
#     else:
#         break
# 
# # Release everything if job is finished
# cap.release()
# out.release()
# cv2.destroyAllWindows()
