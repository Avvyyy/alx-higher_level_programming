#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  args.sort(function (a, b) { return b - a; });
  console.log(args[1]);
}
