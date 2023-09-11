#!/usr/bin/node

const args = parseInt(process.argv.slice(2)[0]);

function printSquare(args) {
  if (isNaN(args)) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < args; i++) {
      let row = '';
      for (let j = 0; j < args; j++) {
        if (i === j || j === args - i - 1) {
          row += 'X';
        } else {
          row += ' ';
        }
      }
      console.log(row);
    }
  }
}

printSquare(args);
