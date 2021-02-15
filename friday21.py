import pyttsx3
import webbrowser
import smtplib,ssl 
import random
import speech_recognition as sr
from time import ctime
import wikipedia
import datetime
import wolframalpha
import os
import sys
from playsound import playsound
import pyautogui # pip install pyautogui
import psutil # pip install psutil
import pyjokes


engine = pyttsx3.init()

client = wolframalpha.Client(' 2RX228-KWEXT6PLTT')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print("Friday:" + audio)
    engine.say(audio)
    engine.runAndWait()


name = "Arnav"

def greetme():
    speak("Hello" + " " + name)
    print('Say your command')


def greetme2():
    speak("Anything else??")

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print('You : ' + said + '\n')
        except Exception:
            print(Exception)

    return said.lower()

def give_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        said = r.recognize_google(audio)
        print('You : ' + said + '\n')

    return said.lower()    

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:/Screenshots")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent )   

def jokes():
    speak(pyjokes.get_joke())


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("You can speak now!!")

        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('You : ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry boss! I didn\'t get that! Try typing!')
        query = str(input("Type Here : "))

    return query.lower()

def sendEmail():
    speak("Please enter the following credentials")
    sender_email = "thefridayassistant@gmail.com"
    rec_email = input(str("Email:"))
    password = 'uwantit??'
    message = ('I am friday here is your email: ' + ' Hello ,' + rec_email )


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()   
    server.login(sender_email, password)
    speak('I logged in !')
    server.sendmail(sender_email, rec_email, message)
    print('email sent sucessfully to ' + rec_email)

WAKE = "friday"

while True:
    print("Listning...")
    query = get_audio() 

    if query.count(WAKE) > 0:
        speak("Yes boss?")
        query = myCommand()
        
        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            speak("here's youtube")

        elif 'open google' in query:
            webbrowser.open('www.google.co.in')
            speak("here's google:")

        elif 'say this' in query:
            speak("what should i say?")
            this = myCommand
            speak(this)  

        elif 'open gmail' in query:
            webbrowser.open('mail.google.com')
            sys.exit()
        
        elif "take a screenshot" in query:
            screenshot()   

        elif "screenshot" in query:
            screenshot()     

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            try:
                sendEmail()
                say("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')       

        elif "who are you" in query:
            speak("did i forget to introduce myself??")
            speak("anyway, i am friday,your personal assistant")
            
        elif 'email me' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')
            

                    
        elif 'email my father' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')

        elif 'email to' in query:
            try:
                sendEmail()
                speak("email was sent sucessfully")     
            except:
                speak('the mail could not b sent due to some problems')       

        elif "bye" in query:
            speak("Byeee!")
            speak("if u want me again, just say : Friday")

        elif "you are mad " in query:
            speak ('sorry boss will not do it again,perhaps never')   

        elif "what is the time" in query:
            speak("the time is:")
            speak(ctime())

        elif 'hello' in query:
            speak('Hello boss')

        elif 'bye' in query:
            speak('Bye ' + " " + name + ', have a good day.')
            sys.exit()
                                        
        elif 'play music' in query:
            speak('Here is your music! Enjoy!')
            webbrowser.open('https://music.amazon.in/my/playlists/Fav/73669e57-3261-4f56-a694-d9e513124650')
            sys.exit()    
                
        elif "where is" in query:
            data = query.split(" ")
            location = data[2]
            location1 = data[3]
            speak("Hold on boss, I will show you where " + location + " " + location1 + " is.")
            url = 'https://www.google.nl/maps/search/' + location + " " + location1 + "/&amp;"
            webbrowser.open(url)
        elif "search wikipedia " in query:
            results = wikipedia.summary(query, sentences=2)
            speak('Got it.')
            speak('WIKIPEDIA says - ')
            speak(results)

        elif "stop" in query:
            speak("ok,just run me when u want me ")    
            sys.exit()


        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('https://www.google.com/search?q=' + query )
                speak("here's what i got on google :")
        
