import audioop
import math
import time

import SpeakEasy.app.pkgs.speech_recognition as sr
import pyaudio
import soundmeter
import librosa


class LangRecog:
    def callback(self, recog, audio):
        timeStart = time.time()
        try:
            recognized_text = recog.recognize_google(audio, language=self.language, show_all=False)
            print("You said: " + recognized_text)
            self.text = recognized_text
            timeEnd = time.time() - timeStart
            print(timeEnd)
        except LookupError:
            print("Unrecognized")
        else:
            print("something else")

    def __init__(self, lang):
        self.text = ""
        self.recognizer = sr.Recognizer()
        self.language = lang

    def listen_and_transcribe(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone(0)
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, 1)
            print("Listening for speech in other languages...")
        stop_listening = recognizer.listen_in_background(source=source, callback=self.callback, phrase_time_limit=30)
        # Unregister the listener and stop the recognizer
        time.sleep(2)
        stop_listening(wait_for_stop=True)

        return self.text

    def setLanguage(self, lang):
        self.language = lang


def hi():
    l = LangRecog("es_US")
    print(l.listen_and_transcribe())


hi()
