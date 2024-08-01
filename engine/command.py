import pyttsx3
import speech_recognition as sr
import eel
import time


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        eel.DisplayMessage("Say that again please...")
        takeCommand()
        return ""
    return query

@eel.expose
def allCommands():
    query = takeCommand()
    query = query.lower()
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
    else:
        print("i don't run")
    
    eel.ShowHood()