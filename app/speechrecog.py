import time

import pkgs_edited.speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone(1)


class LangRecog:
    def callback(self, recog, audio):
        try:
            self.time = time.time() - self.time
            recognized_text = recog.recognize_google(audio, language=self.language, show_all=False)
            print("You said: " + recognized_text)
            self.text = recognized_text
        except LookupError:
            print("Unrecognized")
        except sr.UnknownValueError:
            self.text = ""
            return
        else:
            print("")

    def __init__(self, lang):
        self.text = ""
        self.recognizer = sr.Recognizer()
        self.language = lang
        self.time = None

    def listen_and_transcribe(self):

        with microphone as source:
            print("Listening for speech in other languages...")
        self.time = time.time()
        stop_listening = recognizer.listen_in_background(source=source, callback=self.callback, phrase_time_limit=30)
        # Unregister the listener and stop the recognizer
        time.sleep(3)
        stop_listening(wait_for_stop=True)

        return self.text, self.time

    def setLanguage(self, lang):
        self.language = lang

    def calculateDensityScore(self):
        splitted_string = self.text.split(" ")
        return float(len(splitted_string)) / self.time

    def adjust(self):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source=source)


def hi():
    l = LangRecog("en_US")
    l.listen_and_transcribe()
    return

# hi()
