#!/usr/bin/node
const args = process.argv;

if (!parseInt(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let i = 0; i < parseInt(args[2]); i++){
      process.stdout.write('+');
    }
    console.log()
  }
}
