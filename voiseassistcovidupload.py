import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif  hour>=12 and hour <18:
        speak("Good Afternoon!") 
    else:
        speak("Good Night!")               
    speak("Hi . How can I help you?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogonizing...")
        query = r.recognize_google(audio, language='en-in') #hi-IN en-in
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"  
    return query          



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'test' in query:   
            try:
                speak("opening covid-19 infection prediction system")
                driver = webdriver.Chrome("chromedriver.exe")#chrome driver path
                driver.maximize_window()  
                driver.get("URL TO BE OPENED")# ENTER URL OF THE APP
                time.sleep(2)

                openstate = driver.find_element_by_xpath("//*[contains(text(),'COVID 19')]").text
                print(openstate)
                speak(openstate)

                age = driver.find_element_by_id("age")
                speak("Age of the person")
                content = takeCommand() 
                age.send_keys(content)

                speak("below are some details required, please speak YES or NO ")
                time.sleep(1)


                fever = driver.find_element_by_id("fever")
                speak("do you have fever") 
                content = takeCommand().upper()
                fever.send_keys(content)
                time.sleep(1)

                cough = driver.find_element_by_id("cough")
                speak("do you have cough")
                content = takeCommand().upper()
                cough.send_keys(content)
                time.sleep(1)

                shortnessofbreath = driver.find_element_by_id("shortnessofbreath")
                speak("do you have shortness of breath") 
                content = takeCommand().upper()
                shortnessofbreath.send_keys(content)
                time.sleep(1)

                sorethroat = driver.find_element_by_id("sorethroat")
                speak("do you have sore throat") 
                content = takeCommand().upper()
                sorethroat.send_keys(content)
                time.sleep(1)

                musclepain = driver.find_element_by_id("musclepain")
                speak("do you have pain in muscles?") 
                content = takeCommand().upper()
                musclepain.send_keys(content)
                time.sleep(1)

                nausea = driver.find_element_by_id("nausea")
                speak("do you have nausea ?") 
                content = takeCommand().upper()
                nausea.send_keys(content)
                time.sleep(1)

                diarrhoea = driver.find_element_by_id("diarrhoea")
                speak("do you have diarrhoea ?") 
                content = takeCommand().upper()
                diarrhoea.send_keys(content)
                time.sleep(1)

                fatigue = driver.find_element_by_id("fatigue")
                speak("do you have fatigue ?") 
                content = takeCommand().upper()
                fatigue.send_keys(content)
                time.sleep(1)

                vomiting = driver.find_element_by_id("vomiting")
                speak("do you have vomiting ?") 
                content = takeCommand().upper()
                vomiting.send_keys(content)
                time.sleep(1)

                headache = driver.find_element_by_id("headache")
                speak("do you have headache ?") 
                content = takeCommand().upper()
                headache.send_keys(content)
                time.sleep(1)

                submit = driver.find_element_by_xpath("//*[@class= 'btn btn-success']")
                submit.click()
                speak("Here is the result")
                time.sleep(1)

                infectpercent = driver.find_element_by_xpath("//*[contains(text(),'infection')]").text
                print(infectpercent)
                speak(infectpercent)
                madeby = driver.find_element_by_xpath("//*[contains(text(),'Made')]").text
                print(madeby)
                speak(madeby)
                time.sleep(1)
                speak("Going Back")
                goback = driver.find_element_by_xpath("//*[@class= 'btn btn-success my-2 my-sm-0']")
                goback.click()
                
            except Exception as e:
                print(e)
                speak("sorry could not predict")

                                 
            

                           