#!/usr/bin/node
const args = process.argv;
const len = args.length;
let biggest;
let sec_biggest = 0;

if (len > 3) {
  biggest = args[2];

  for (let i = 2; i < len; i++) {
    if (args[i] > biggest) {
      sec_biggest = biggest;
      biggest = args[i];
    } else if (args[i] > sec_biggest) {
      sec_biggest = args[i];
    }
  }
}
console.log(sec_biggest);
