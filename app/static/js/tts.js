function TTS(text, lang) {
    if(text === " "){
        return;
    }
    let speech = new SpeechSynthesisUtterance();
    speech.lang = lang;
    speech.text = text;
    speech.rate = 1;
    speech.pitch = 0.8;
    let voices = []; // global array

      // Get List of Voices
    voices = window.speechSynthesis.getVoices();

      // Initially set the First Voice in the Array.

    for(i = 0; i < voices.length; i++){
        speech.voice = voices[i];
        window.speechSynthesis.speak(speech);
    }

}


document.getElementById("speech").addEventListener("click", function(){
    TTS("Hola. Voy al supermercado. Ha sido un día divertido.", "es-ES");
})