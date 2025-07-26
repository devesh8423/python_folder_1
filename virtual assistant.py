import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3  # convert text to speech
import pyaudio
import webbrowser
import os
# while(1):
engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id )
engine.setProperty('rate',200)
# engine.say('Good morrning boss,how are you?')
# engine.runAndWait()  # loop

def speak(msg):
    engine.say (msg)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good mornig boss!")
    elif(hour>=12 and hour<18):
        speak("Good afternoon boss!")
    else:
        speak("Good evening boss")
    speak("I am your virtual assistant how may i help you ?")

def takeCommand():
    r=sr.Recognizer() # recognise class helps in recognize the audio
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=0.5 # it refers to the amount of time gap
        r.energy_threshold=300 # noise cancellation
        audio=r.listen(source)

    try:
        print("Recognising..")
        query=r.recognize_google(audio,language="en-in")
        print("user Said:",query)
    except Exception as e:
        print("Say that again please!")
        return "None"
    


wishMe()
if 1:
    query=takeCommand().lower()
    if 'wikipedia' in query:
        speak("Searching wikipidia")
        query=query.replace("wikipedia","")
        result=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)
    elif 'youtube'in query:
        webbrowser.open("youtube.com")
    elif 'stack overflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'google' in query:
        query=query.replace("google","")
        query=query.replace("search","")
        webbrowser.open("https://www.google.com/search?q=" +query)
    elif (("music" in query) or ("song" in query)):
        music_dir="d://oldsongs"
        songs=os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif "time" in query:
        time=datetime.datetime.now().strftime("%h:%m")
        speak("Sir,The time is")
    elif 'sleep' in query:
        speak("Thankyou")
        exit()
    else:
        print("Invalid Literal!")