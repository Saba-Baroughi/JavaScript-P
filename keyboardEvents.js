// Note: We pass the event to the function to get info about it!
function handleKeys(event) {
  let pressedDiv = document.getElementById("key-pressed");
  let downDiv = document.getElementById("key-down");
  let upDiv = document.getElementById("key-up");
  let currentKeySpan = document.getElementById("current-key");
  let lastKeySpan = document.getElementById("last-key");

  if (event.repeat) {
    return false; // prevents holding the key from triggering the event again
  } else {
    if (event.type === "keydown") {
      downDiv.style.backgroundColor = "lightgreen";
      pressedDiv.style.backgroundColor = "lightgreen";
      currentKeySpan.innerHTML =
        event.key + " (" + event.code + " / " + event.keyCode + ")";
    } else if (event.type === "keyup") {
      currentKeySpan.innerHTML = "";
      downDiv.style.backgroundColor = "white";
      pressedDiv.style.backgroundColor = "white";
      upDiv.style.backgroundColor = "lightgreen";

      // This just changes the upDiv back to white after 75ms
      setTimeout(function () {
        upDiv.style.backgroundColor = "white";
      }, 75);

      lastKeySpan.innerHTML =
        event.key + " (" + event.code + " / " + event.keyCode + ")";
    }
  }
}
