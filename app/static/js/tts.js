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
    
    speech.voice = voices[0];
    window.speechSynthesis.speak(speech);

}
function authenticate(){
    window.onload = function () {
    google.accounts.id.initialize({
      client_id: 'YOUR_GOOGLE_CLIENT_ID',
      callback: handleCredentialResponse
    });
    google.accounts.id.prompt();
  };
}

document.getElementById("speech").addEventListener("click", function(){
    TTS("Hola. Voy al supermercado. Ha sido un día divertido.", "es-ES");
})