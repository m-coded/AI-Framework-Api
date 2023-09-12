import pyttsx3
import speech_recognition as sr
#import pyaudio
import datetime
import subprocess
import wikipedia
import smtplib
import pywhatkit
#from flask import Flask, request
#from pywhatkit.remotekit import start_server
from email.message import EmailMessage
import smtplib
import requests
import os
import subprocess

 
 


 
engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 9)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def greatMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning {user}")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon  ")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening , {user} ")
        print("Hello,Good Evening")
    speak(' how  are  you ? marvellous')
    speak("oh,oh ,sorry sir , how are  you sir")

 
    
 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
     r.pause_threshold = 2
     r.adjust_for_ambient_noise(source, duration=1)
     audio = r.listen(source)

    try:
            print("Listening...")
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

    except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
    return statement

 
 
 
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(statement):
 try:

  results = wikipedia.summary(statement, sentences=5)

 
  return (results)
 except:
    pass

 
def play(video):
    pywhatkit.playonyt(video)

def search_on_google(statement):
    pywhatkit.search(statement)

def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+234{number}", message)

def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = email
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(email, email)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

api="4dbc17e007ab436fb66416009dfb59a8"

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
   

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]