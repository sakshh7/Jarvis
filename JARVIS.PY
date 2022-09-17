from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voices",voices[0].id)

def speak(audio):

    engine.say(audio)
    print(audio)
    engine.runAndWait()
#convert voice into text    
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        r.pause_threshold=3
        audio =r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")
    except Exception as e:
        speak("say that again please...")
        return "none"
    return query
#wish function  
def wish() :
    hour=int(datetime.datetime.now().hour)
    
    if hour>0 and hour<12:
        speak("Good Morning")
    elif hour>12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("good afternoon")
    speak("hy my name is jarvis how can i help you")

if __name__=="__main__":
    # speak("  namaste my name his sakshi . she is very beautiful")
    #takecommand()
    wish()
    # while True:
    if 1:
        query=takecommand().lower()
        if "open notepad"in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow("webcam",img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir="C:\\Users\\DELL\\Music"
            songs=os.listdir(music_dir)
            rd=random.chice(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif "ip address" in query:
            ip=get("https://api.ipify.org").text
            speak(f"your ip addres is{ip}")
        elif "wikipedia" in query:
            speak("searching wikipedia....")
            query=query.replace("wikkipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open('www.youtube.com')
        elif "open linkdin " in query:
            webbrowser.open("www.linkdin.com")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
        elif "open google" in query:
            speak("mam what should i search on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        elif "send message " in query:
            pywhatkit.sendwhatmsg("+917489492180", "this is testing protocol",1,51)
        elif "play song on youtube" in query:
            speak("sure mam")
            pywhatkit.playonyt("love me like you do")
            
            