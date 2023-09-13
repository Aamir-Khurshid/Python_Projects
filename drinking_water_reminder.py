import time
import pyttsx3

text_speak = pyttsx3.init()
while True:
    command = "Drink Water my friend"
    text_speak.say(command)
