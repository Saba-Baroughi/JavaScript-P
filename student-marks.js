let students = [
  {
    name: "John",
    subjects: ["maths", "english", "cad"],
    teacher: { maths: "Harry", english: "Joan", cad: "Paul" },
    results: { maths: 90, english: 75, cad: 87 },
  },
  {
    name: "Emily",
    subjects: ["science", "maths", "english", "art"],
    teacher: { science: "Iris", maths: "Harry", english: "Joan", art: "Simon" },
    results: { science: 93, maths: 95, english: 80, art: 95 },
  },
  {
    name: "Adam",
    subjects: ["science", "maths", "art"],
    teacher: { science: "Iris", maths: "Harry", art: "Simon" },
    results: { science: 63, maths: 79, art: 95 },
  },
];
const averagePoints = (arr, subject) => {
  let totalMarks = 0;
  let numberOfStudents = 0;

  for (const student of arr) {
    //for (let i = 0; i < arr.length; i++) {
    //     const student = arr[i];

    //     if (subject in student.results) {
    //       totalMarks += student.results[subject];
    //       numberOfStudents++;
    //     }
    //   }
    //// Check if the student has results for the specified subject
    // if (student.results.hasOwnProperty(subject)) {
    //     // Do something if the subject exists in the results
    //   }
    if (subject in student.results) {
      totalMarks += student.results[subject];
      numberOfStudents++;
    }
  }

  return numberOfStudents === 0 ? 0 : totalMarks / numberOfStudents;
};

let averageMarks = averagePoints(students, "english");
console.log(averageMarks);
