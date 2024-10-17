import pyttsx3
import speech_recognition
import datetime


engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour= int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<=12:
        speak("Good Morning, sir")
    elif hour>12 and hour <=16:
        speak("Good Afternoon, sir")
        
    else:
        speak("Good Evening, sir")

    speak("how are you?, sir")    
         

