import pyaudio
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello Sir i am your virtual assistant")
engine.runAndWait()