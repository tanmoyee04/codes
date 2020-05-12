# -*- coding: utf-8 -*-
"""
Created on Sun May  3 22:23:07 2020

@author: Tanmoyee
"""

import pyttsx3 #to import speech
import datetime #preinstalled in python
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser #inbuilt module in python for opening browser and youtube
import os #for your pc related purpose like playing music etc
#import smtplib #to send mails via gmail
import smtplib #for sending emails
engine=pyttsx3.init('sapi5') #inbuilt voice API by windows
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour) #since jarvis is gonna wish me by seeing the time
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am a jarvis and my name is shreya. please tell me how can i help you?")
    
def takeCommand(): #it takes microphone input from the user and returns string output
    r=sr.Recognizer() #it recognizes the voice
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1 #i have changed the time rather increased it 
        audio=r.listen(source)
    try:
        print("Recognizing....")
        query=r.recognize_google(audio)
        print("User said : ",query)
    except Exception as e:
        print(e)
        print("Say that again please......")
        return "None" #returns none when some problem occurs
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() #specifies local host
    server.starttls() #for the connection
    server.login('your mail id','my_password')
    server.sendmail('your mail id',to,content)
    server.close()
    
if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
    # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2) #returns 2 sentences from wikipedia
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open("https://www.youtube.com/")
        elif 'open whatsapp' in query:
            speak('opening whatsapp...')
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open google' in query:
            speak('opening google...')
            webbrowser.open("https://www.google.com/")
        elif 'open github' in query:
            speak('opening github...')
            webbrowser.open("https://github.com/")
        elif 'open linkedin' in query:
            speak('opening linkedin...')
            webbrowser.open("https://www.linkedin.com/feed/")
        elif 'open stackoverflow' in query:
            speak('opening stack overflow...')
            webbrowser.open("https://stackoverflow.com/")
        elif 'open facebook' in query:
            speak('opening facebook...')
            webbrowser.open("https://www.facebook.com/")
        elif 'open google classroom' in query:
            speak('opening google classroom...')
            webbrowser.open("https://classroom.google.com/h")
        elif 'open WAC' in query:
            speak('opening what after college...')
            webbrowser.open("https://wac.thinkific.com/pages/coming_soon")
        elif 'todays weather' in query:
            speak('opening todays weather report...')
            webbrowser.open("https://www.accuweather.com/en/in/durgapur/191572/weather-forecast/191572")
        elif 'corona updates' in query:
            speak('opening the corona updates...')
            webbrowser.open("https://www.mygov.in/covid-19")
        elif 'play music' in query:
            music_dir='C:\\Users\\Tanmoyee\\music'
            songs=os.listdir(music_dir) #lists all the songs present in my directory here
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S") #for converting time to string
            speak(f"the time is {strTime}")
        elif 'open dev c' in query:
            codePath="C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe"
            os.startfile(codePath)
        elif 'email to tanmoyee' in query:
            try:
                speak("what should I send in that email?")
                content=takeCommand()
                to="your_mail_id"
                sendEmail(to,content)
                speak("your email has been sent.")
            except Exception as e:
                print(e)
                speak("sorry dear , i am unable to send this email")
        