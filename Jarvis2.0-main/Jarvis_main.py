import pyttsx3 #pip install pyttsx3
import speech_recognition #pip install SpeechRecognition
import requests #pip install requests
import datetime
import os
from bs4 import BeautifulSoup #pip install beautifulsoup4
import pyautogui
import webbrowser
from time import sleep
import random

engine = pyttsx3.init()
voices = engine.getProperty("voices") #microsoft inbuilt voices
engine.setProperty("voice", voices[0].id) #David voice
rate = engine.setProperty("rate",180) #speech rate in words per minute
pitch = engine.setProperty("pitch",150)
volume = engine.setProperty("volume",2)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1 #take some pause after listening
        r.energy_threshold = 300
        audio = r.listen(source,0,4) #after every 4 pause it will act , wont stop on just listening

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def whatsappMsg(name,msg):
    pyautogui.press("super")
    pyautogui.typewrite(query)
    pyautogui.sleep(2)
    pyautogui.press("enter")
    sleep(5)
    pyautogui.click(x=196, y=149)
    pyautogui.write(name)
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.click(x=237, y=214)
    sleep(2)
    pyautogui.click(x=1075, y=986)
    pyautogui.write(msg)
    pyautogui.press('enter')


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in Ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in Ahmedabad"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "what is the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to "+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=v-icNVDbVLk")
                    if b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=pxCWiYFkvTg")
                    if b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=DCkRJ8BDRQU")
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "whatsapp" in query:
                    speak("to whom sir?")
                    name = input("Enter the name: ")
                    speak(f'what is the message for{name}')
                    msg = takeCommand()
                    whatsappMsg(name,msg)

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break