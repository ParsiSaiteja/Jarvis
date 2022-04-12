import winsound                        
import instaloader                     # It DOWNLOADS PUBLIC AND PRIVATE PROFILES, HASHTAGS, USER STORIES, FEEDS AND SAVED MEDIA.
import pyttsx3                         # It IS USED TO CONVERT TEXT TO SPEECH
import pywhatkit                       # IT IS USED TO SEND A MESSAGE TO WHATSAPP GROUP OR CONTACT
import pyaudio                         # IT IS USED TO SUPPORT THE AUDIO. PYAUDIO IS ONLY SUPPORTED ON PYTHON 3.6 VERSION.
import requests                        # IT IS USED TO SEND AN HTTP REQUEST
import speech_recognition as sr        # IT IS USED TO RECOGNISE THE SPEECH
import datetime                        # IT IS USED TO SET THE DATE AND TIME
import os                              
import cv2
import random
import webbrowser
import wikipedia
from requests import get
import smtplib
import sys
import time
import instadownloader
from bs4 import BeautifulSoup
import time
import datetime
from playsound import playsound
#import MyAlarm
from pywikihow import search_wikihow
import psutil
import speedtest
import pyautogui
import screen_brightness_control as screen
import PyPDF4
import datefinder
import query
import wolframalpha

# text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good  morning , its {tt}")
    elif hour > 12 and hour < 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak('i am jarvis sir, please tell me how can i help you')


# To send Email
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('yourmail id' , 'password')
    server.sendmail('sendermail id' , to , content)
    server.close()


# To fetch the news
def news():
    mainurl = 'https://newsapi.org//v2//top-headlines?sources=techcrunch&apikey=ec6b12c741de41308e0686fa035a773e'
    mainpage = requests.get(mainurl).json()

    articles = mainpage["articles"]

    head = []
    day = ["first","second","third","fourth","fifth","sixth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is : {head[i]}")


# To read the audiobook
def pdf_reader():
    book = open('python.pdf', 'rb')
    pdfReader = PyPDF4.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages}")
    speak("Sir please enter the page number which i have to read")
    pg = int(input("Please enter the page number :"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


# To Convert voice to text
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening..')
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        command = r.recognize_google(audio)
        print(f"user said: {command}")

    except Exception as e:
        #speak("Say that again please")
        return "none"
    return command


def TaskExecution():
#if __name__ == '__main__':
    wish()
    while True:
        # if 1:

        command = take_command().lower()

        # Logic Building for tasks

        # It opens notepad
        if 'open notepad' in command:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)

        # It opens command prompt
        elif 'open command prompt' in command:
            os.system('start cmd')

        # To close the cmd
        elif 'close command prompt' in command:
            os.system('taskkill /f /im cmd.exe')
            speak("okay sir, closing command prompt")

        elif 'are you single' in command:
            speak('no i am in relationship with wifi')

        # It opens a camera
        elif 'open camera' in command:
            cap = cv2.VideoCapture(0)
            while True:
                ret , img = cap.read()
                cv2.imshow('webcam', img)
                q = cv2.waitKey(100)
                if q == 50:
                    break;
                cap.release()
                cv2.destroyAllWindows()

        # It plays the music content which are available in system
        elif 'play music' in command:
            music_dir = "E:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir , rd))

        # It is used to check the ip address of the system
        elif 'ip address' in command:
            ip = get('https://api.ipify.org').text
            speak(f"Your Ip address is {ip}")

        # search the data through wikipedia
        elif 'wikipedia' in command:
            speak('searching wikipedia')
            command = command.replace("wikipedia" , "")
            result = wikipedia.summary(command , sentences=1)
            speak("According to wikipedia")
            speak(result)
            print(result)

        # It opens a YouTube
        elif "open youtube" in command:
            webbrowser.open("www.youtube.com")

        # It opens a Facebook
        elif "open facebook" in command:
            webbrowser.open("www.facebook.com")

        # It opens a Google and ask a query
        elif "open google" in command:
            speak("sir, what should i search in google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")

        # It plays a song in YouTube
        elif "play" in command:
            #speak("which song shall i play")  #WE CAN USE THIS CASE WHILE THE SYSTEM HAS GIVEN THE RESPONSE
            #song = take_command().lower()
            song = command.replace("play","")
            speak("playing song in youtube" + song)
            pywhatkit.playonyt(song)

        # It sends a message through WhatsApp
        elif "send message" in command:
            pywhatkit.sendwhatmsg("+91xxxxxxxxxx" , "This is testing protocol" , 15 , 11)
            speak("Message has been sent")

        # It sends a mail
        elif "send email to person" in command:
            try:
                speak("what should i say")
                content = take_command().lower()
                to = "xxxxxxxx@gmail.com"
                sendEmail(to , content)
                speak("Email has sent to the person")

            except Exception as e:
                print(e)
                speak("Sorry email has not sent to the person")

        # To close the notepad application
        elif "close notepad" in command:
            speak("okay sir closing notepad")
            os.system("taskkill /f /im notepad.exe")

        # To Tell the time
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"the time is {time}")

        # To Check A instagram profile
        elif "instagram" in command:
            speak("Sir, please enter the username correctly")
            name = input("Enter username here :")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of the user {name}")
            #time.sleep(10)
            speak("Sir would you like to download profile picture of this account")
            condition = take_command().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name , profile_pic_only=True)
                speak("i am done sir, profile picture is saved in our main folder, now i am ready for next command")
            else:
                pass

        # To take a screenshot
        elif "take screenshot" in command:
            speak("sir, please tell me the name for this screenshot file")
            name = take_command().lower()
            speak("please sir, hold the screen for few seconds, i am taking screenshot")
            #time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder, now i am ready for next command")

        # To know the location of ours using ip address
        elif "where we are" in command or "what is the location" in command:
            speak("wait sir, let me check")
            try:
              ipAdd = requests.get('https://api.ipify.org').text
              print(ipAdd)
              url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
              geo_requests = requests.get(url)
              geo_data = geo_requests.json()
              #print(geo_data)
              city = geo_data['city']
              #state = geo_data['state']
              country = geo_data['country']
              speak(f"Sir i am not sure, but i think we are in {city} city of {country} country")
            except Exception as e:
              speak("sorry sir i am not able to find our location")
              pass

        # To Know the weather forecast
        elif "temp" in command:
            search = "temperature in Nizamabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"current {search} is {temp}")

        # To set an alarm
        elif "alarm" in command:
            #speak("sir please tell me at what time  should set an alarm, for example, set alarm at 5:30pm ")
            #tt = take_command().lower()   # set alarm to 5:30am
            #tt = tt.replace("set alarm at", "")   # 5:30a.m.
            #tt = tt.replace(".","")   # 5:30AM
            #tt = tt.upper()
            #import MyAlarm
            #MyAlarm.alarm(tt)
            speak("enter the time")
            time = input("Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Time to wake up sir !")
                    winsound.PlaySound('ratsasan.mp3',winsound.SND_LOOP)
                    speak("Alarm closed!")

                elif now>time:
                    break

        # To search on chrome
        elif "search on chrome" in command:
            speak("what should i search sir")
            search = take_command().lower()
            chromepath = 'C://Program Files//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chromepath).open_new_tab(search+'.com')

        # To close the chrome
        elif "close chrome" in command:
            speak("okay sir, closing google chrome")
            os.system("taskkill /f /im chrome.exe")
            
        # To search anything by using activate mode by speech recognition
        elif "activate" in command:
            speak("how to mode is activated please tell me what you want to know")
            #search = input("enter the text: ")
            how = take_command().lower()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            print(how_to[0])
            speak(how_to[0].summary)
            speak("the steps has been completed")

        # To read the news
        elif "tell me news" in command:
            speak("Please wait sir , fetching the latest news")
            news()
            speak("The news has been completed")

        # To check the battery percentage
        elif "how much battery we have" in command or "how much power we have" in command or "battery" in command:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage} have battery")
            if percentage>=60:
                speak("We have enough battery to work")
            elif percentage>=30 and percentage<=59:
                speak("We have to connect to our charging point")
            elif percentage>=16 and percentage<=29:
                speak("We don't have enough power to work")
            elif percentage<=15:
                speak("We have low power to work, please connect to the charging, the system will shutdown very soon")

        # To check the internet speed
        elif "internet speed" in command:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

        # To say the wishes
        elif "wishes" in command:
            speak('Happy Birthday Mummy, You are the most special person in my life. I love you from the deepest core of my heart.Have a gorgeous happy birthday.I love you maa.' )
            speak('Happy Birthday maa')
            music_dir = "E:\\Musics"
            songs = os.listdir(music_dir)
            # rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir , song))

        # To Set the volumes
        elif 'volume up' in command:
            pyautogui.press('volumeup')
        elif 'volume down' in command:
            pyautogui.press('volumedown')
        elif 'volume mute' in command:
            pyautogui.press('volumemute')

        # To set the brightness
        elif "set brightness to maximum" in command:
            screen.set_brightness(100)
        elif "set brightness to medium" in command:
            screen.set_brightness(50)
        elif "set brightness to minimum" in command:
            screen.set_brightness(20)

        # To calculate the variables
        elif "calculate" in command:
            from Main1 import calculator
            speak("what should i calculate")
            #speak("Enter the two variables what should I calculate")
            cal = take_command().lower()
            #cal = input("Enter the two variables with the operations :")
            calculator(cal)

        # To check the temperature through WolframAlpha
        elif "outside weather" in command:
            from Main1 import temp
            speak("Sir tell me which place I should check the temperature")
            #speak("Enter the place where should I check the weather")
            temp_res = take_command().lower()
            #temp_res = input("Enter the text :")
            temp(temp_res)
        #else:
            #from Main1 import wolfRam
            #result = wolfRam(cal)
            #speak(result)

        # To open specific folders from our system
        elif "elders folder" in command:
            speak("opening notepad")
            os.startfile('C:\\Users\\user\\OneDrive\\Desktop\\Notepad.txt')

        elif "movies folder" in command:
            speak('opening movies folder')
            os.startfile('E:\\MOVIES')

        elif "python folder" in command:
            speak('opening pycharm projects folder')
            os.startfile('C:\\Users\\user\\PycharmProjects')

        elif "download folder" in command:
            speak('opening download folder')
            os.startfile('C:\\Users\\user\\Downloads')

        elif "close folder" in command:
            speak("okay sir, closing elders folder")
            os.system("taskkill /f /im notepad.exe")

        # To open & close specific Microsoft Office files
        elif 'microsoft excel' in command:
            speak('opening microsoft excel')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk')
        elif 'close excel' in command:
            speak('closing microsoft excel')
            os.system('taskkill /f /im excel.exe')

        elif 'microsoft powerpoint' in command:
            speak('opening microsoft powerpoint')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007.lnk')
        elif 'close powerpoint' in command:
            speak('closing microsoft powerpoint')
            os.system('taskkill /f /im powerpnt.exe')

        elif 'microsoft outlook' in command:
            speak('opening microsoft outlook')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Outlook 2007.lnk')
        elif 'close outlook' in command:
            speak('closing microsoft outlook')
            os.system('taskkill /f /im outlook.exe')

        elif 'microsoft onenote' in command:
            speak('opening microsoft onenote')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office OneNote 2007.lnk')
        elif 'close one note' in command:
            speak('closing microsoft onenote')
            os.system('taskkill /f /im onenote.exe')

        elif 'microsoft word' in command:
            speak('opening microsoft word')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk')
        elif 'close word' in command:
            speak('closing microsoft word')
            os.system('taskkill /f /im WINWORD.EXE')

        elif 'microsoft access' in command:
            speak('opening microsoft access')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Access 2007.lnk')
        elif 'close access' in command:
            speak('closing microsoft access')
            os.system('taskkill /f /im MSACCESS.EXE')

        elif 'microsoft publisher' in command:
            speak('opening microsoft publisher')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Publisher 2007.lnk')
        elif 'close publisher' in command:
            speak('closing microsoft publisher')
            os.system('taskkill /f /im MSPUB.EXE')

        elif 'microsoft groove' in command:
            speak('opening microsoft groove')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Groove 2007.lnk')
        elif 'close groove' in command:
            speak('closing microsoft groove')
            os.system('taskkill /f /im GROOVE.EXE')

        elif 'microsoft infopath' in command:
            speak('opening microsoft infopath')
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office InfoPath 2007.lnk')
        elif 'close infopath' in command:
            speak('closing microsoft infopath')
            os.system('taskkill /f /im INFOPATH.EXE')

        # To open adobe reader
        elif 'adobe reader' in command:
            speak('opening adobe reader')
            os.startfile('C://ProgramData//Microsoft//Windows//Start Menu//Programs//Adobe Reader 8.lnk')
        # To close adobe reader
        elif 'close adobe' in command:
            speak('closing adobe')
            os.system('taskkill /f /im AcroRd32.exe')

        # To open Microsoft Edge
        elif 'microsoft edge' in command:
            speak('opening microsoft edge')
            os.startfile('C:\\Users\\user\\OneDrive\\Desktop\\Microsoft Edge.lnk')

        # To open calculator application
        elif 'open calculator app' in command:
            speak('opening calculator application')
            os.startfile('calc.exe')
        # To close calculator
        elif 'close calculator' in command:
            speak('closing calculator application')
            os.system('taskkill /f /im calc.exe')

        # To shut down the system
        elif "shutdown the system" in command:
            os.system("shutdown /s /t 5")

        # To Restart the system
        elif "restart the system" in command:
            os.system("restart /r /t 5")

        # To Sleep the system
        elif "sleep the system" in command:
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

        elif "hello" in command:
            speak("Hello sir, how may i help you")

        elif "how are you" in command:
            speak("i am fine sir what about you")

        elif "thanks" in command or "thank you" in command:
            speak("it's my pleasure sir")

        elif "you can sleep" in command or "take a break" in command:
            speak("Okay sir i am going to take a break, you can call me anytime")
            break

if __name__=='__main__':
    while True:
        command1 = take_command().lower()
        if "wake up" in command1:
            TaskExecution()
        elif "sleep" in command1 or "exit" in command1:
            speak("thanks for using me, have a good day")
            sys.exit()
