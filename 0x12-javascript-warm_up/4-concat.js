#!/usr/bin/node

const args = process.argv.slice(2);
const a = args[0];
const b = args[1];

function printArgs (a, b) {
  console.log(a + ' is ' + b);
}

printArgs(a, b);
