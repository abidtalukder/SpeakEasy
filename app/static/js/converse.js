function updateText(val) {
    if (val == "Sorry, I didn't get that. Please record again.") {
        document.getElementById("speakButton").innerHTML = val;   
    } else {
        document.getElementById("latestUserSpeech").value = val;   
    }
}
    
  // creating message elements

function createUserMessageElement(message) {
    // Create the elements
    const liElement = document.createElement('li');
    liElement.classList.add('d-flex', 'justify-content-between', 'mb-4');

    const divCard = document.createElement('div');
    divCard.classList.add('card', 'mask-custom', 'w-100');

    const cardHeader = document.createElement('div');
    cardHeader.classList.add('card-header', 'd-flex', 'justify-content-between', 'p-3');
    cardHeader.style.borderBottom = '1px solid rgba(255, 255, 255, 0.3)';

    const userTitle = document.createElement('p');
    userTitle.classList.add('fw-bold', 'mb-0');
    userTitle.textContent = 'User';

    const timeText = document.createElement('p');
    timeText.classList.add('text-light', 'small', 'mb-0');
    // You can set time or any other text here if needed

    const cardBody = document.createElement('div');
    cardBody.classList.add('card-body');

    const mainText = document.createElement('p');
    mainText.classList.add('mb-0');
    mainText.textContent = message; // Replace the default text with the provided message

    const avatarImage = document.createElement('img');
    avatarImage.src = 'https://mdbcdn.b-cdn.net/img/Photos/Avatars/avatar-5.webp';
    avatarImage.alt = 'avatar';
    avatarImage.classList.add('rounded-circle', 'd-flex', 'align-self-start', 'ms-3', 'shadow-1-strong');
    avatarImage.width = '60';

    // Build the structure
    cardHeader.appendChild(userTitle);
    cardHeader.appendChild(timeText);
    cardBody.appendChild(mainText);
    divCard.appendChild(cardHeader);
    divCard.appendChild(cardBody);
    liElement.appendChild(divCard);
    liElement.appendChild(avatarImage);

    // Replace the existing element with the created one
    return liElement;
}

function createBotMessageElement(message) {
    // Create the new list item element
    var li = document.createElement('li');
    li.className = 'd-flex justify-content-between mb-4';

    // Create the image element
    var img = document.createElement('img');
    img.src = 'https://cdn3.iconfinder.com/data/icons/avatars-9/145/Avatar_Robot-512.png';
    img.alt = 'avatar';
    img.className = 'rounded-circle d-flex align-self-start me-3 shadow-1-strong';
    img.width = '60';

    // Create the div element with the card structure
    var cardDiv = document.createElement('div');
    cardDiv.className = 'card mask-custom';

    // Create the card header div
    var cardHeader = document.createElement('div');
    cardHeader.className = 'card-header d-flex justify-content-between p-3';
    cardHeader.style.borderBottom = '1px solid rgba(255, 255, 255, 0.3)';

    // Create the title paragraph inside card header
    var titlePara = document.createElement('p');
    titlePara.className = 'fw-bold mb-0';
    titlePara.textContent = 'SpeakEasy Companion';

    // Create the message paragraph inside card header
    var messagePara = document.createElement('p');
    messagePara.className = 'text-light small mb-0';
    messagePara.textContent = message; // Replace the text with the provided message

    // Create the card body div
    var cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    // Create the paragraph inside the card body
    var bodyPara = document.createElement('p');
    bodyPara.className = 'mb-0';
    bodyPara.textContent = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.';

    // Construct the element hierarchy
    cardHeader.appendChild(titlePara);
    cardHeader.appendChild(messagePara);
    cardBody.appendChild(bodyPara);
    cardDiv.appendChild(cardHeader);
    cardDiv.appendChild(cardBody);
    li.appendChild(img);
    li.appendChild(cardDiv);

    return li;
}

function addBotMessage(message) {
    var history = document.getElementById('conversationHistory');
    history.appendChild(createBotMessageElement(message));
}

function addUserMessage(message) {
    var history = document.getElementById('conversationHistory');
    history.appendChild(createUserMessageElement(message));
}

// Replace the existing element with the newly created one

  function getGPTResponse() {
    $.ajax({
      type: "POST",
      url: "/gptResponse",
      data: {
        speech: $("#latestUserSpeech").val(),
      },
      success: function (response) {
        if (response != "None") {
          addBotMessage(response);
        } else {
          updateText("Bot Fail. Please Record Again.");
        }
      },
    });
  }

  function recordConversation() {
    $(document).on("click", "#speakButton", function (e) {
      console.log("hello");
      e.preventDefault();
      $.ajax({
        type: "POST",
        url: "/userResponse",
        success: function (response) {
          if (response != "None") {
            updateText(response);
            addUserMessage(response);
            getGPTResponse();
          } else {
            updateText("Sorry, I didn't get that. Please record again.");
          }
        },
      });
    });
  }
  
  recordConversation();
//   addUserMessage("Hello, I am your SpeakEasy Companion. How can I help you today?");