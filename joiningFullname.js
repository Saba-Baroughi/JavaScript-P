const persons = [
  { firstname: "Malcom", lastname: "Reynolds" },
  { firstname: "Kaylee", lastname: "Frye" },
  { firstname: "Jayne", lastname: "Cobb" },
];

let result = persons.map(getFullName);

function getFullName(item) {
  return [item.firstname, item.lastname].join(" ");
}
console.log(result);

function points(games) {
  // Initialize the total points to 0
  let totalPoints = 0;

  // Iterate through each match result in the games array
  for (let i = 0; i < games.length; i++) {
    // Split the match result into our team's score (x) and opponent's score (y)
    let [x, y] = games[i].split(":").map(Number);

    // Calculate points based on the match result
    if (x > y) {
      // Win: 3 points
      totalPoints += 3;
    } else if (x === y) {
      // Tie: 1 point
      totalPoints += 1;
    }
    // Loss: 0 points (no need for an explicit condition as it's the default)
  }

  return totalPoints;
}

// Example usage:
const matchResults = [
  "3:1",
  "2:2",
  "0:4",
  "4:0",
  "1:0",
  "3:3",
  "2:1",
  "0:0",
  "1:2",
  "4:2",
];
const teamPoints = points(matchResults);
console.log(`Total points: ${teamPoints}`);
