import wolframalpha     # BY USING WOLFRAMALPHA WE CAN CHECK THE TEMPERATURE, WE CAN CALCULATE AND CHECK THE APIID
import pyttsx3          # IT IS USED TO CONVERT THE TEXT TO SPEECH

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To create a Wolfram App id:
def wolfRam(query):
    api_key = "R8ALLE-PAK9U5H76T"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer

    except:
        speak("An String Value Is Not Answerable")


# To calculate from WolframAlpha
def calculator(query):
    term = str(query)

    term = term.replace("jarvis","")
    term = term.replace("plus","+")
    term = term.replace("minus","-")
    term = term.replace("multiply","*")
    term = term.replace("divide","/")

    final = str(term)

    try:
        result = wolfRam(final)
        speak(f"{result}")
    except:
        speak("An String Value Is Not Answerable")


# To check the temperature using WolfRamAlpha
def temp(query):
    term = str(query)

    term = term.replace("jarvis","")
    term = term.replace("in","")
    term = term.replace("what is the","")
    term = term.replace("temperature","")

    temp_query = str(term)

    if 'outside' in temp_query:
        var1 = "temperature in"
        answer = wolfRam(var1)
        speak(f"{var1} is {answer}")

    else:
        var2 = "temperature" + temp_query
        answer1 = wolfRam(var2)
        speak(f"{var2} is {answer1}")

# We can also use this process to check the temperature        
#temp('temperature london')

        #elif "temp" in command:
            #from Main1 import temp
            #temp(query)

        #else:
            #from Main1 import wolfRam
            #result = wolfRam(query)
            #speak(result)
