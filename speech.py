import sl4a
import time

droid = sl4a.Android()

def speak(text):
    droid.ttsSpeak(text)
    while droid.ttsIsSpeaking()[1] == True:
        time.sleep(1)

def listen(text):
    return droid.recognizeSpeech(text,None,None)[1]
