<script src="https://apis.google.com/js/platform.js" async defer></script>
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
function authenticate(){
    window.onload = function () {
    google.accounts.id.initialize({
      client_id: 'YOUR_GOOGLE_CLIENT_ID',
      callback: handleCredentialResponse
    });
    google.accounts.id.prompt();
  };
}