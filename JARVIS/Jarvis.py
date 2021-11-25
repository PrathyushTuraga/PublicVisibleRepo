import json
import os
import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import requests
import pywhatkit as kit
import smtplib

# Below 2 lines are for setting voice for JARVIS from voices available for windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
#print(voices[0].id)
# print(voices[1].id)

# We will set user name as Tony and this can be changed anytime
author = "Tony"

# This function is used when we want JARVIS to say something to user
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# This function is used for sending mail through gmail
def sendEmail(to, content):
    # -> Here you need to login to your gmail account, navigate to "https://myaccount.google.com/security" and enable
    #    feature "Less secure app access".
    # -> Below lines are standard for accessing gmail smtp server. We will open smtp
    #    connect, send mail and then close the connection.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your gmail address', 'your password')
    server.sendmail('your gmail address', to, content)
    server.close()

# This function is used for greeting the user at the start of session.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # Based on hour, JARVIS will greet the user accordingly.
    if 0 <= hour < 12:
        speak(f"Good Morning {author}")
    elif 12 <= hour < 18:
        speak(f"Good Afternoon {author}")
    else:
        speak(f"Good Evening {author}")
    speak(f"Hello {author} I am Jarvis, Please tell me how may I help you")

# This function is used to take voice input from user
def takeCommand():
    """
    Here you might get error that pyaudio is missing.
    Even if you try to install pyaudio with command "pip install pyaudio", it could give error.
    For this issue you can take whl file from page "https://www.lfd.uci.edu/~gohlke/pythonlibs/"
    according to your python version and install it with command
    pip install PyAudio‑0.2.11‑cp310‑cp310‑win_amd64.whl
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        # pause_threshold is used for time gap in seconds to detect words separately.
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query} \n")
    except Exception as e:
        print(f"Sorry {author}, Say That again...")
        return "None"
    return query

# Main function for program
if __name__ == "__main__":
    # speak(f"Welcome {author}, I am Jarvis")
    wishMe()
    # takeCommand()
    # Below line will run function one time. If you want multiple times use while statement
    if 1:
        query = takeCommand().lower()
        # Below if condition will take first 2 sentences from wikipedia and reads out to user.
        if 'wikipedia' and 'who' in query:
            speak("Speak Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        # Below else if condition will take latest news from newsapi.org website and will read out to user.
        # For this, user need to create account on newsapi.org website and substitute his apikey below.
        elif 'news' in query:
            speak("News Headlines")
            query = query.replace("news", "")
            url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=<YourApiKeyHere>"
            news = requests.get(url).text
            news = json.loads(news)
            art = news['articles']
            # For understanding below structure you can check API documentation on website.
            # We are extracting only required elements from JSON output of API call.
            for article in art:
                print(article['title'])
                speak(article['title'])
                print(article['description'])
                speak(article['description'])
                speak("Moving on to next news")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
        elif 'search browser' in query:
            speak("What should i search ?")
            um = takeCommand().lower()
            webbrowser.open(f"{um}")
        # Below else if condition will give your system public ip address by checking on 'api.ipify.org' website.
        elif 'ip address' in query:
            ip = requests.get('http://api.ipify.org').text
            print(f"Your ip is {ip}")
            speak(f"Your ip is {ip}")
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open brave' in query:
            codepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codepath)
        elif 'play music' in query:
            # Below lines will navigate to music directory, list all files and play first file (mp3)
            music_dir = 'C:\\Users\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'play youtube' in query:
            speak("What should i search in youtube?")
            cm = takeCommand().lower()
            kit.playonyt(f"{cm}")
        elif 'send message' in query:
            # Below lines will send message through web.whatsapp.com
            # Below using below code, you need to first login to whatsapp from your web browser.
            speak("Who do you want to send the message ?")
            num = input("Enter number : \n")
            speak("What do you want to send ?")
            msg = takeCommand().lower()
            H = int(input("Enter hour? \n"))
            M = int(input("Enter Minutes ? \n"))
            kit.sendwhatmsg(num, msg, H, M)
        elif 'send email' in query:
            # Below code will send mail from gmail through smtp connection
            speak(f"What should i send {author} ?")
            content = takeCommand().lower()
            speak(f"Whom to send the email, enter email address {author}")
            to = input("Enter email address: \n")
            # Below function is defined in the starting lines of code.
            sendEmail(to, content)
