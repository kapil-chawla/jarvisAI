from playsound import playsound
import eel

#plays assistant sound
@eel.expose
def playAssistantSound():
    playsound('www/assets/audio/start_sound.mp3')