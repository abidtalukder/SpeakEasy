import time

import speech_recognition as sr


class LangRecog:
    def callback(self, recog, audio):
        try:
            recognized_text = recog.recognize_google(audio, language=self.language, show_all=False)
            print("You said: " + recognized_text)
            self.text = recognized_text
        except LookupError:
            print("Unrecognized")

    def __init__(self):
        time.sleep(0.1)
        self.text = ""
        self.recognizer = sr.Recognizer()
        self.language = "en_US"

    def listen_and_transcribe(self):
        recognizer = sr.Recognizer()
        microphone = sr.Microphone(0)
        with microphone as source:
            print("Listening for speech in other languages...")
            recognizer.adjust_for_ambient_noise(source)

        stop_listening = recognizer.listen_in_background(source=source, callback=self.callback, phrase_time_limit=10)
        time.sleep(2)
        # Unregister the listener and stop the recognizer
        stop_listening(wait_for_stop=True)
        return self.text

    def setLanguage(self, lang):
        self.language = lang
        
caller = LangRecog()
print(caller.listen_and_transcribe())
