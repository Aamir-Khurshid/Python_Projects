import pyttsx3

text_speech = pyttsx3.init()
answer = []
n = int(input("The no. of people : "))
for i in range(0, n):
    names = input()
    answer.append(names)

for i in answer:
    text_speech.say(f"Shoutout to {i}")

text_speech.runAndWait()