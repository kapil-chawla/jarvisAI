from playsound import playsound
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

from engine.helper import extract_yt_term, remove_words

#plays assistant sound
@eel.expose
def playAssistantSound():
    playsound('www/assets/audio/start_sound.mp3')
    
    
def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("What do you want me to open?")
    
def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)