function updateText(val) {
    document.getElementById("convo").innerHTML = val;
    document.getElementById("latestUserSpeech").value = val;
  }

  function getGPTResponse() {
    $.ajax({
      type: "POST",
      url: "/gptResponse",
      data: {
        speech: $("#latestUserSpeech").val(),
      },
      success: function (response) {
        if (response != "None") {
          updateText("GPT: " + response);
        } else {
          updateText("Sorry, I didn't get that. Please record again.");
        }
      },
    });
  }

  function recordConversation() {
    $(document).on("click", "#speech", function (e) {
      console.log("hello");
      e.preventDefault();
      $.ajax({
        type: "POST",
        url: "/userResponse",
        success: function (response) {
          if (response != "None") {
            updateText(response);
            getGPTResponse();
          } else {
            updateText("Sorry, I didn't get that. Please record again.");
          }
        },
      });
    });
  }