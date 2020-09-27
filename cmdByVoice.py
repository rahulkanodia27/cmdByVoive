#!/usr/bin/python3


print("content-type: text/html")
print()

import pyttsx3
import cgi
import speech_recognition as sr

pyttsx3.speak("Welcome,This is your system assistent")
pyttsx3.speak("May i help you")

r = sr.Recognizer()

with sr.Microphone() as source:
     print("start saying...")
     audio = r.listen(source)
     print("we got it,plz wait...")
p = r.recognize_google(audio)

while True:
     if (("run" in p) or  ("execute" in p )) and ("chrome" in p):
       sp.getoutput("chrome")
     elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
       sp.getoutput("notepad")

     elif (("run" in p) or  ("execute" in p )) and (("player" in p) and ("media" in p)):
       sp.getoutput("wmplayer")

     elif (("run" in p) or  ("execute" in p )) and ("file explorer" in p):
       sp.getoutput("explorer")

     elif (("run" in p) or  ("execute" in p )) and ("calculater" in p):
       sp.getoutput("calc")

     elif (("run" in p) or  ("execute" in p )) and ("character map" in p):
       sp.getoutput("charmap")

     elif (("run" in p) or  ("execute" in p )) and ("paint" in p):
       sp.getoutput("mspaint")

     elif (("run" in p) or  ("execute" in p )) and ("task manager" in p):
       sp.getoutput("taskmgr")

       
     elif  ("exit" in p)  or ("quit" in p):
         break

     else:
       print("dont support")
       break


