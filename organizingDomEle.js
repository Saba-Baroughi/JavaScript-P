// Get the body and all the rows
let tbody = document.getElementsByTagName("tbody")[0];
let rows = tbody.children;

// Set up the array to hold our people
let people = [];

// Iterate through all rows, "build" a person, and push them into the array
for (let row of rows) {
  let person = {};

  let cells = row.children;
  person.name = cells[0].textContent;
  person.age = cells[1].textContent;
  person.favoriteFood = cells[2].textContent;
  people.push(person);
}

// Voila!
console.log("People:\n", people);

// Now you can do anything you want...find people who love steak!
let steakLovers = people.filter(function (person) {
  return person.favoriteFood === "Steak";
});
console.log("\nPeople who love steak:\n", steakLovers);

// Sort by age (see https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)
let sortedPeople = people.sort(function (a, b) {
  return a.age - b.age;
});
console.log("\nSorted people:\n", sortedPeople);

// Get the name of the youngest person
let youngest = sortedPeople[0].name;
console.log("\nYoungest person is:", youngest);

// Or using something more complex, like Array.prototype.reduce()
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
oldest = people.reduce(function (currentOldest, person) {
  return person.age > currentOldest.age ? person : currentOldest;
});
console.log(`${oldest.name}, the oldest, is ${oldest.age} years old`);
