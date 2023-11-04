import time

import speech_recognition as sr


def on_audio(audio, recognizer):
    try:
        recognized_text = recognizer.recognize_google(audio, language="auto")
        print("You said: " + recognized_text)
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")


def listen_and_transcribe():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(0)

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source=source)
        print("Listening for speech in other languages...")

    stop_listening = recognizer.listen_in_background(microphone, on_audio)

    time.sleep(2)
    # Unregister the listener and stop the recognizer
    stop_listening(wait_for_stop=True)


listen_and_transcribe()
