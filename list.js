function buildTableData() {
  // Grab the data from the table in the HTML
  let table = document.querySelector("table");
  let rows = table.querySelectorAll("tbody tr");

  // Initialize an empty array to store the objects
  let data = [];

  // Iterate through the rows
  rows.forEach(function (row) {
    // Add the parameter 'row' here
    let columns = row.querySelectorAll("td");

    // Build an object for each row and push it to the array
    let rowData = {
      name: columns[0].textContent,
      rating: columns[1].textContent,
      review: columns[2].textContent,
    };

    data.push(rowData);
  }); // Add closing parenthesis for forEach loop

  // Return the completed array
  return data;
}

// Outside the function, declare a variable named data
// and assign it the returned value from the buildTableData function
var data = buildTableData();

// Log the value of the data variable to the console
console.log(data);
