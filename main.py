import os 
import eel

eel.init("www")
os.system("start msedge.exe --app http://localhost:8080/index.html")
eel.start("index.html", mode=None, host="localhost", port=8080, block=True)