import speech_recognition as sr
from gtts import gTTS
import playsound
import os


#collect name and purpose of the visitor
def ask_name():
    UserVoiceRecognizer = sr.Recognizer()
    name = ""
                
    flag = True
                
    
    #ask_name = "Please state your name"
    #audio = gTTS(text=ask_name, lang="en", slow=False)
    #audio.save("name.mp3")
    #os.system("play name.mp3")
                
    #while flag:
     #   try:
      #      with sr.Microphone() as UserVoiceInputSource:
                #UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.3)
                    
                # The Program listens to the user voice input.
                #UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
                    
               # name = UserVoiceRecognizer.recognize_google(UserVoiceInput)
              #  name = name.lower()
                                
             #   with open("audio_file.wav", "wb") as file:
            #        file.write(UserVoiceInput.get_wav_data())
           #         print('File saved')
                                

          #      print(f"Name: {name}")
                                
         #       flag = False
        #except KeyboardInterrupt:
           # print()
          #  exit(0)
        #except sr.UnknownValueError:
         #   print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
    
    return 'prath'

def ask_purpose():
    UserVoiceRecognizer = sr.Recognizer()
    purpose = ""
                
    flag = True
                
    #ask_purpose = "Please state your purpose"
    #audio = gTTS(text=ask_purpose, lang="en", slow=False)
    #audio.save("purpose.mp3")
    #os.system("play purpose.mp3")
                
    #while flag:
        #try:
            #with sr.Microphone() as UserVoiceInputSource:
                #UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.3)
                
                # The Program listens to the user voice input.
                #UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
                
              #  purpose = UserVoiceRecognizer.recognize_google(UserVoiceInput)
               # purpose = purpose.lower()

          #      print(f"Purpose: {purpose}")
         #       flag = False
        #except KeyboardInterrupt:
          #  print()
         #   exit(0)
        #except sr.UnknownValueError:
            #print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
                
    return 'to eat'