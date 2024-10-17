from os import system
import pyttsx3
import pyaudio
import speech_recognition

engine =pyttsx3.init("sapi5")
voices =engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone()as source:
        print("listening....")
        r.pause_threshold=1
        r.energy_threshold=200
        audio=r.listen(source,0,4)
    
    try:
         print("Understanding...")
         query=r.recognize_google(audio,language='en-in')
         print(f"You Said :{query}\n")
    
    except Exception as e:
        print("Say that Again")
        return "none"
    
    return query

if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up" or "wake up " in query:
            from Greet_me import greetMe
            greetMe()

            while True:
                query=takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime ")
                    break
                elif "hello" in query:
                    speak("Hello sir, how are you")
                elif "i am fine" in query:
                    speak("that's great sir")    
                elif "how are you" in query:
                    speak("Fully Charged,") 
                elif "thank you" in query:
                    speak("you're welcome, sir")
                elif "good night" in query:
                    speak("Good Night")
                    break