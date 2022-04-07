import pyttsx3    # IT IS USED TO CONVERT THE TEXT TO SPEECH 
import pyaudio    # IT IS USED TO SUPPORT THE AUDIO

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

for voice in voices:
    print(voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello Sir i am your virtual assistant")
engine.runAndWait()
