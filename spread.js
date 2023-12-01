let students = [
  {
    name: "John",
    subjects: ["maths", "english", "cad"],
    teacher: { maths: "Harry", english: "Joan", cad: "Paul" },
    results: { maths: 90, english: 75, cad: 87 },
  },
  {
    name: "Emily",
    subjects: ["science", "english", "art"],
    teacher: { science: "Iris", english: "Joan", art: "Simon" },
    results: { science: 93, english: 80, art: 95 },
  },
  {
    name: "Adam",
    subjects: ["science", "maths", "art"],
    teacher: { science: "Iris", maths: "Harry", art: "Simon" },
    results: { science: 63, maths: 87, art: 95 },
  },
];

let subjects = [...students[0].subjects]; // Using the spread operator to copy the subjects array

const update = (item, val) => [...item, val]; // it is a new array with added val which is Electronics
//here as the simple function used we just [...item, val] otherwise {}

let updatedSubjects = update(subjects, "Electronics");

console.log(updatedSubjects);
console.log(students[0]);
