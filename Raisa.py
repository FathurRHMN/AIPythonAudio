from unittest import result
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#import pyaudio


print("Inisializing Raisa")

MASTER = "Fathur"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


#Speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak ("Good Morning" + MASTER)
    elif hour >= 12 and hour <= 18:
        speak ("Good Afternoon" + MASTER)            
    else :
        speak ("Good Evening" + MASTER)
        speak ("")

        
#microphone 
def takeComand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said :{query}\n")

    except Exception as e:
         speak("Say that again please" + MASTER)
         query = query.lower()

    return query     


# main Start Here
speak("Hello my name is Raisa, I can help you!" + MASTER)
wishMe()
query = takeComand()

# System Logic For Task as Question Query
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)

elif "youtube" in query.lower():
    url = "www.youtube.com"
    # chrome_path =  "C:/Program Files/Google/Chrome/Application/chrome.exe %s" 
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url)

elif "movie" in query.lower():
    url = "nontonanimeid.moe"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url)

elif "whatsapp web" in query.lower():
    url = "web.whatsapp.com"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url)

elif "felony" in query.lower():
    url = "rekrutmen.pelni.co.id"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url) 

elif "my jobs" in query.lower():
    url = "rekrutmenbersama.fhcibumn.id/login_page"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url) 

elif "wings" in query.lower():
    url = "join.wings.co.id"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url) 

elif "jobs" in query.lower():
    url = "lokerbumn.com/lowongan-kerja"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s" 
    webbrowser.get(chrome_path).open(url)     

elif "gmail" in query.lower():
    url = "mail.google.com/mail/u/2/#imp"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s"  
    webbrowser.get(chrome_path).open(url)       

elif "instagram" in query.lower():
    url = "www.instagram.com"
    chrome_path =  "C:/Program Files/Mozilla Firefox/firefox.exe  %s"  
    webbrowser.get(chrome_path).open(url)         

elif "music" in query.lower():
    # songs_dir = "C:\\Users\\HP\\Desktop\\Lagu"
    songs_dir = "C:\\Users\\HP\\Music\\Playlists"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif "time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} The time is {strTime}")

elif "who are you" in query.lower():
         speak('I am your personal Assistant Raisa')

elif 'what can you do for me' in query.lower():
         speak('I can play songs, tell time, and can help you' + MASTER)


# else : speak("Can help you"+ MASTER)
