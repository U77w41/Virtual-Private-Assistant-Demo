# Importing Necessary files
import pyttsx3

engine = pyttsx3.init("sapi5")  # The speech engine sapi5 created my microsoft
voices = engine.getProperty('voices') # storing the voices inside a variable
engine.setProperty('voices',voices[0].id) # setting the voice id 0 ,1 ,2 .....
engine.setProperty('rate',170) # speech rate 200 as a normal speed

# Creating a function to speak a given text

def Say(TEXT):
    print('             ')
    print(f'A.I. : {TEXT}')
    engine.say(text = TEXT)
    engine.runAndWait()
    print("             ")

#Say('Hello World')