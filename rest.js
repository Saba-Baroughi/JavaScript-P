let mixedLetters = ["b", "d", "a", "c", "f", "e"];
//it was given we write the rest

let moreMixedLetters = [...mixedLetters, "h", "k", "g", "j", "i", "l"];

console.log(moreMixedLetters);

const updateSortReverse = (arr, ...letters) =>
  [...arr, ...letters].sort().reverse();
// In summary, ...arr is used to include the elements from an existing array,
// and ...letters is used to include additional elements from the function
//parameters,and together they form a new array.

let reverseSort = updateSortReverse(moreMixedLetters, "n", "m", "o");

console.log(reverseSort);
console.log(mixedLetters);
