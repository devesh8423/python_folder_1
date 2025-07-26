import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Try to select a female voice if available
for v in voices:
    if 'female' in v.name.lower():
        engine.setProperty('voice', v.id)
        break
else:
    engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)

def speak(msg):
    print("Assistant:", msg)
    engine.say(msg)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning boss!")
    elif hour < 18:
        speak("Good Afternoon boss!")
    else:
        speak("Good Evening boss.")
    speak("I am your virtual assistant. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        return r.recognize_google(audio, language="en-in")
    except Exception as e:
        print("Could not understand audio:", e)
        speak("I didn't catch that, please repeat.")
        return None

if __name__ == "__main__":
    wishMe()
    while True:
        if (q := takeCommand()) and (q := q.lower()):
            query = q
            print("User said:", query)

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "").strip()
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(result)
                    speak(result)
                except Exception as e:
                    speak("Sorry, I couldn't find anything.")

            elif 'youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            elif 'stack overflow' in query:
                speak("Opening Stack Overflow")
                webbrowser.open("https://stackoverflow.com")

            elif 'google' in query:
                speak("Searching Google")
                search = query.replace("google", "").replace("search", "").strip()
                webbrowser.open("https://www.google.com/search?q=" + search)

            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {current_time}")

            elif 'music' in query or 'song' in query:
                music_dir = "d://oldsongs"
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in your music directory.")

            elif 'sleep' in query or 'exit' in query:
                speak("Thank you. Bye!")
                break

            else:
                speak("Sorry, I didn't understand that.")
        # else: skip iteration silently until a valid command is received
