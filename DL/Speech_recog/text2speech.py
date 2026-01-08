#pip install pyttsx3
import pyttsx3
txt_sp=pyttsx3.init()
voices = txt_sp.getProperty('voices')
txt_sp.setProperty('voice', voices[1].id)
volume=txt_sp.getProperty('volume')
txt_sp.setProperty('volume',0.8)
rate=txt_sp.getProperty('rate')
txt_sp.setProperty('rate',125)
text=input("enter text here:")
txt_sp.say(text)
txt_sp.runAndWait()
txt_sp.stop()