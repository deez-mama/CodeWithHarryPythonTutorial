# Program to import any module and use it

# The following code imports the pyttsx3 module and uses it to convert text to speech.

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello World!")
engine.runAndWait()