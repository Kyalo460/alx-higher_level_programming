#!/usr/bin/node
const args = process.argv;
const len = args.length;
let biggest;
let secBiggest = 0;

if (len > 3) {
  biggest = args[2];

  for (let i = 3; i < len; i++) {
    if (args[i] > biggest) {
      secBiggest = biggest;
      biggest = args[i];
    } else if (args[i] > secBiggest) {
      secBiggest = args[i];
    }
  }
}
console.log(secBiggest);
