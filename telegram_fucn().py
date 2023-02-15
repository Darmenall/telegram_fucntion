import speech_recognition as sr  # pip install SpeechRecognition
from googletrans import Translator  # pip install googletrans==3.1.0a0
import pyttsx3  # pip install pyttsx3

translator = Translator()
engine = pyttsx3.init()

mic = sr.Microphone(device_index=1)
r = sr.Recognizer()

while True:
    input("говорите на русском сперва нажмите ENTER")
    with mic as source:
        audio = r.listen(source)
    try:
        d = r.recognize_google(audio, language="ru-RU")
        print("Google Speech Recognition thinks you said " + d)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    if d == "Отставить":
        break
    perevod = translator.translate(d, dest="en")

    engine.setProperty('rate',150)
    engine.setProperty('volume',0.9)

    engine.say(perevod.text)
    engine.runAndWait()


