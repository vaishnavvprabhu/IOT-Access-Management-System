from uuid import uuid4
from datetime import datetime
import requests

from appwrite.client import Client
from appwrite.services.storage import Storage
from appwrite.input_file import InputFile
from appwrite.permission import Permission
from appwrite.role import Role

import RPi.GPIO as GPIO
import time

#! /usr/bin/python

# import the necessary packages
# from imutils.video import VideoStream
# from imutils.video import FPS
# import face_recognition
# import imutils
# import pickle
# import time
# import cv2
# import numpy as np
# from picamera import PiCamera
# import pyautogui

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 

import speech_recognition as sr
from gtts import gTTS
import playsound
import os

from picamera import PiCamera
from time import sleep

import askName
import askPurpose
import FaceCamera

# #Initialize 'currentname' to trigger only when a new person is identified.
# currentname = "unknown"
# #Determine faces from encodings.pickle file model created from train_model.py
# encodingsP = "encodings.pickle"


def lookCamera():
    '''
        Ask user to look into camera
    '''
    UserVoiceRecognizer = sr.Recognizer()
    
    look = "Please look into the camera and smile"
    audio = gTTS(text=look, lang="en", slow=False)
    audio.save("lookMessage.mp3")
    os.system("play lookMessage.mp3")

def goodToGo():
    '''
        Play this message after collecting name, purpose, etc.
    '''
    UserVoiceRecognizer = sr.Recognizer()
    
    good = "Thank you! Please wait for sometime for the access approval"
    audio = gTTS(text=good, lang="en", slow=False)
    audio.save("goodMessage.mp3")
    os.system("play goodMessage.mp3")

def entryAllowed(name, purpose):
    '''
        Play this when entry is approved
    '''
    UserVoiceRecognizer = sr.Recognizer()
    allowance = ""
    
    message = f"Welcome {name}, your entry is approved for the purpose of {purpose}"
    
#     welcome = "Welcome "
#     approve = " Your entry is approved for the purpose of: "
#     allowance = welcome+name+approve+purpose
    
    audio = gTTS(text=message, lang="en", slow=False)
    audio.save("welcomeMessage.mp3")
    os.system("play welcomeMessage.mp3")


endPoint = "https://backend.vaishnavvp.ml/v1"
projectId = "6326f911ae375aa5307e"
appwriteApiKey = "efe0078df86ed1867daf844459d884079a7f89496b4ab98033a5b48e22fe8e0a07ea1763cdc41e5e2ec243015d42e43371a5e23ff1295e9c81cb1c686e759032071b625de7f6d850bb4d7515aa08bc17d346e29ca6e081d63330c6adc3e302b2173792b17f62a8065018daecd8d943dbd1eb651d4b6fa4ec394a1359b8f196c1"
restApiKey = "8HR7QUBW7BVXJID4"

# create instance of client using endpoint, projectid and appwrite api key
client = Client()
(client
    .set_endpoint(endPoint)
    .set_project(projectId)
    .set_key(appwriteApiKey)
)

# create instance of storage
storage = Storage(client)

sensor = 16
LED = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,False)
print("IR Sensor Ready.....")
print(" ")

try:
    while True:
        if GPIO.input(sensor):
            
            GPIO.output(LED, False)
            
            
        else:
            GPIO.output(LED, True)
            #GPIO.output(LED, GPIO.HIGH)
            print("Object Detected")
            
            # create a unique id and current date and time
            id = str(uuid4())
            date, time = str(datetime.now()).split('.')[0].split(' ')

            name = askName.ask_name()
            purpose = askPurpose.ask_purpose()
            
            lookCamera()
            
            FaceCamera.camera(name, id)
            
            # upload video to appwrite
            storage.create_file("6345607d09612196e5aa", 
                id, 
                InputFile.from_path(f"{id}.avi"), 
                permissions=[Permission.read(role=Role.any()), 
                        Permission.delete(role=Role.user('6326f8b1e632914619b5')),
                        Permission.update(role=Role.user('6326f8b1e632914619b5'))
                    ]
                )
            
            # upload image to appwrite
            storage.create_file("633c30143c8b6adcd208", 
                id, 
                InputFile.from_path("vaishnav.jpg"), # CHANGE FILE NAME ONCE IMAGE CAPTURE IS DONE
                permissions=[Permission.read(role=Role.any()), 
                        Permission.delete(role=Role.user('6326f8b1e632914619b5')),
                        Permission.update(role=Role.user('6326f8b1e632914619b5'))
                    ]
                )
            
            # create image URL to push to API
            imgURL = f"https://backend.vaishnavvp.ml/v1/storage/buckets/633c30143c8b6adcd208/files/{id}/view?project=6326f911ae375aa5307e"
            
            # create API URL for POST request
            apiURL = f"http://backend.vaishnavvp.ml:3000/update?key={restApiKey}&field1={id}&field2={name.title()}&field3={purpose.capitalize()}&field4={date}&field5={time}&field6={imgURL}&field7={id}"
            # AUDIO STUFF NOT DONE YET (I THINK)
            
            # push visit details to database
            res = requests.post(apiURL)
            if res.status_code == 200:
                print("Upload done..")
            else:
                print("Something went wrong while uploading to database..")
            
            goodToGo()
            entryAllowed(name, purpose)
            
            break
            
#             while GPIO.input(sensor):
#                 time.sleep(0.2)
            
    


except KeyboardInterrupt:
    GPIO.cleanup()
    



