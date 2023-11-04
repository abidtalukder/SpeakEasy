document.getElementById("speech").addEventListener("click", function(){
    var speech = true;
    window.speechRecognition = window.speechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeecRecognition();
    
    recognition.interimResults = true;
    recognition.addEventListener('result', e => {
        const transcript = Array.from(e.results)
        .map(result => result[0])
        .map(result => result.transcript)
        
        document.getElementById("voices").innerHTML = transcript;
    })
    
    if (speech = true) {
        recognition.start();
    }
    
})