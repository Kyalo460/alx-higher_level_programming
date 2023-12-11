#!/usr/bin/node
const args = process.argv;

function factorial (a) {
  if (a === 0 || !a) {
    return 1;
  }

  return a * factorial(a - 1);
}

console.log(factorial(args[2]));
