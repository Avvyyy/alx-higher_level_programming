#!/usr/bin/node

const args = process.argv.slice(2);

function argMessage (args) {
  if (!args[0]) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
}

argMessage(args);
