#!/usr/bin/node
// Reads and prints lines in a file
const args = process.argv.slice(2);
const fs = require('fs');

const file = args[0];
fs.readFile(file, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
        return;
    }

    const lines = data.split('\n');
    lines.forEach(line => console.log(line));
});
