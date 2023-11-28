let usernames = ["Harry", "Daisy", "Michael", "Sarah", "Sally"];

var form = document.getElementById("registration-form");
form.addEventListener("submit", handleSubmit);
var errorMsg = document.getElementById("errors");

function handleSubmit(event) {
  event.preventDefault();
  var usernameInput = document.getElementById("username");
  var newUsername = usernameInput.value;
  if (usernames.includes(newUsername)) {
    errorMsg.innerHTML =
      "Sorry, the username " +
      newUsername +
      " is already in use. Please choose another username.";
  } else {
    usernames.push(newUsername);
    form.submit();
    console.log(usernames);
  }
}
