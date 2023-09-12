#!/usr/bin/node

const args = parseInt(process.argv.slice(2)[0]);

function printSquare (args) {
  if (isNaN(args)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < args; i++) {
      console.log(('X'.repeat(args)));
    }
  }
}

printSquare(args);
