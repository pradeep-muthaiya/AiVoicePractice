import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS
import pyaudio

print("Sr Version: " + sr.__version__)
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def speak(text): 
    tts = gTTS(text = text, lang = "en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            said = r.recognize_google(audio, show_all=True)
            print("You said: {}".format(said))
        except:
            print("Could Not Recognize Voice")
    return said

p = pyaudio.PyAudio()
print(p.get_device_info_by_index(0)['defaultSampleRate'])

speak("Hello Pradeep")
get_audio()

