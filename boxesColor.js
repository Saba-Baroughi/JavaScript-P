function boxClicked() {
  var currentColor = this.style.backgroundColor;

  this.style.backgroundColor = currentColor === "green" ? "orange" : "green";
  //the same as
  //   if (currentColor === "green") {
  //     this.style.backgroundColor = "orange";
  //   } else {
  //     this.style.backgroundColor = "green";
  //   }
}

let boxes = document.getElementsByClassName("box");
for (i = 0; i < boxes.length; i++) {
  boxes[i].addEventListener("click", boxClicked);
}
