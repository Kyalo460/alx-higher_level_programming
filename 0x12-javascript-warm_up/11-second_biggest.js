#!/usr/bin/node
const args = process.argv;
const len = args.length;
let biggest;
let secBiggest = 0;

if (len > 3) {
  biggest = args[2];
  secBiggest = args[3];

  for (let i = 3; i < len; i++) {
    if (parseInt(args[i]) > biggest) {
      secBiggest = biggest;
      biggest = parseInt(args[i]);
    } else if (parseInt(args[i]) > secBiggest) {
      secBiggest = parseInt(args[i]);
    }
  }
}
console.log(secBiggest);
