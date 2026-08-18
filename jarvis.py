import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()


def speak(*audio):
    text = " ".join(str(part) for part in audio)
    engine.say(text)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is", Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is", day, month, year)


def wishme():
    hour = datetime.datetime.now().hour
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d %m %Y")

    if hour >= 4 and hour < 12:
        greeting = "Good Morning Sir!"
    elif hour >= 12 and hour < 18:
        greeting = "Good Afternoon Sir!"
    elif hour >= 18 and hour < 24:
        greeting = "Good Evening Sir!"
    else:
        greeting = "Good Night Sir!"

    speak(
        "welcome back SIR!",
        "the current time is", current_time,
        "the current date is", current_date,
        greeting,
        "Jarvis at your word. Please tell me how can I help you?"
    )

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        Query = r.recognize_google(audio, language='en-in')
        print(Query)

    except Exception as e :
        print(e)
        speak("Say that again please...")
        return "None"
    
    return Query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(os.getenv("Email ID"), os.getenv("Email Password"))
    server.sendmail(os.getenv("Email ID"), to, content)
    server.close()
    
def screenshot():
    img =  pyautogui.screenshot()
    img.save("C:\\Users\\Administrator\\OneDrive\\Desktop\\jarvis\\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'search in chrome' in query:
            speak("What shouuld I search?")
            chromepath =  "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
            search  =  takeCommand.lower()
            wb.get (chromepath).open_new_tab(search+'.com')
        
        elif 'logout' in query:
            os.system("shutdown -1")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play songs' in query:
            songs_dir = "D:\\Music"
            songs =  os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
        
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("You said me to remember that"+remember.read()) 

        elif 'screenshot' in query:
            speak("Ok sir, what should I name that file?")
            path = takeCommand()
            path1name = path + ".png"
            path1 = "C:\\Users\\Administrator\\OneDrive\\Desktop\\jarvis\\" + path1name
            kk = pyautogui.screenshot()
            kk.save(path1)
            os.startfile("C:\\Users\\Administrator\\OneDrive\\Desktop\\jarvis\\") 
        elif 'screenshot' in query:
            screenshot()
            speak("Done sir!")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()
            
        elif 'offline' in query:
            quit()

