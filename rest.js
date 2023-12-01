let mixedLetters = ["b", "d", "a", "c", "f", "e"];
//it was given we write the rest

let moreMixedLetters = [...mixedLetters, "h", "k", "g", "j", "i", "l"];

console.log(moreMixedLetters);

const updateSortReverse = (arr, ...letters) =>
  [...arr, ...letters].sort().reverse();

let reverseSort = updateSortReverse(moreMixedLetters, "n", "m", "o");

console.log(reverseSort);
console.log(mixedLetters);
