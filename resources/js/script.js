// Code for the changing text at the top of the page
const greetings = [
    { text: "Unlock the World, One Language at a Time", color: "white" },
    { text: "Die Welt entdecken, eine Sprache nach der anderen", color: "blue" },
    { text: "Découvrez le monde, une langue à la fois", color: "red" },
    { text: "Descubre el mundo, un idioma a la vez", color: "green" }
];

let currentIndex = 0;

function changeGreeting() {
    const greetingElement = document.getElementById("greeting");
    currentIndex = (currentIndex + 1) % greetings.length;
    const currentGreeting = greetings[currentIndex];
    greetingElement.textContent = currentGreeting.text;
    greetingElement.style.color = currentGreeting.color;
}

// Change the greeting every 3 seconds
setInterval(changeGreeting, 3000);