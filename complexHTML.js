let books = [
  {
    title: "The Girl With the Dragon Tattoo",
    author: "Stieg Larsson",
    published: 2005,
  },
  {
    title: "Harry Potter and the Goblet of Fire",
    author: "JK Rowling",
    published: 2000,
  },
  {
    title: "Thinking, Fast and Slow",
    author: "Daniel Kahneman",
    published: 2011,
  },
  {
    title: "Days Without End",
    author: "Sebastian Barry",
    published: 2016,
  },
  {
    title: "The Silence of the Girls",
    author: "Pat Barker",
    published: 2018,
  },
];

// Write your code here
// Define the buildTable function
function buildTable() {
  // Initialize the table HTML
  let tableHtml = "<table>";

  // Add the table header
  tableHtml +=
    "<thead><tr><th>Title</th><th>Author</th><th>Published</th></tr></thead>";

  // Add the table body
  tableHtml += "<tbody>";
  books.forEach(function (book) {
    tableHtml +=
      "<tr><td>" +
      book.title +
      "</td><td>" +
      book.author +
      "</td><td>" +
      book.published +
      "</td></tr>";
  });
  tableHtml += "</tbody>";

  // Close the table tag
  tableHtml += "</table>";

  // Return the completed HTML
  return tableHtml;
}

// Outside the function, declare a variable named table
// and assign it the value returned from the buildTable function
var table = buildTable();

// Insert the table variable of HTML into the element with the id of "books-table"
document.getElementById("books-table").innerHTML = table;
