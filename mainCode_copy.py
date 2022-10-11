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

from tts_stt import ask_name, ask_purpose
import FaceCamera as fc

#Initialize 'currentname' to trigger only when a new person is identified.
currentname = "unknown"
#Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

sensor = 16
LED = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(LED,True)
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
 
            name = ask_name()
            purpose = ask_purpose()

            with open('name_purpose.txt', 'w') as file:
                file.write(name)
                file.write(purpose)

            fc.camera(name)
            
            
            
            def entryAllowed():
                UserVoiceRecognizer = sr.Recognizer()
                allowance = ""
                
                welcome = "Welcome "
                approve = " Your entry is approved for the purpose of: "
                allowance = welcome+name+approve+purpose
                audio = gTTS(text=allowance, lang="en", slow=False)
                audio.save("welcomeMessage.mp3")
                os.system("play welcomeMessage.mp3")
            entryAllowed()
            break
            
#             while GPIO.input(sensor):
#                 time.sleep(0.2)
            
    


except KeyboardInterrupt:
    GPIO.cleanup()
    



