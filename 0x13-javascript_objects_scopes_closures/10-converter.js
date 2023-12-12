#!/usr/bin/node
let count = 0;
exports.converter = function (base) {
  return num => num.toString(base);
};
