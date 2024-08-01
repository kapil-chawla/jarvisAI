import os 
import eel

from engine.features import *
from engine.command import *

playAssistantSound()

eel.init("www")
os.system("start msedge.exe --app http://localhost:8080/index.html")
eel.start("index.html", mode=None, host="localhost", port=8080, block=True, size=(800, 600)) 

