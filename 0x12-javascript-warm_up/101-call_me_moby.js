#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  // Executes a function x times
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
