function addSquare() {
  // Create a div element
  let square = document.createElement("div");

  square.classList.add("square");

  document.getElementById("squares-wrapper").appendChild(square);
}

function removeSquare() {
  // the same square which was added here is selected
  let squares = document.getElementsByClassName("square");

  // Check if there's at least one square to remove
  if (squares.length > 0) {
    // Remove the last square
    squares[squares.length - 1].remove();
  }
}
