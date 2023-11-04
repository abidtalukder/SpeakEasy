function TTS(text, lang) {
    if(text === " "){
        return;
    }
    let speech = new SpeechSynthesisUtterance();
    speech.lang = lang;
    speech.text = text;
    speech.rate = 2;
    speech.pitch = 1;
    let voices = []; // global array

      // Get List of Voices
    voices = window.speechSynthesis.getVoices();

      // Initially set the First Voice in the Array.
    speech.voice = voices[0];
    window.speechSynthesis.speak(speech);

}