#!/usr/bin/node

const arg = process.argv.slice(2);
const argN = parseInt(arg[0]);

function printFactorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n <= 1) {
    return (1);
  } else {
    return (n * printFactorial(n - 1));
  }
}

console.log(printFactorial(argN));
