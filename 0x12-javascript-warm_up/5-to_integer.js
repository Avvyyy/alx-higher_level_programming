#!/usr/bin/node

const args = process.argv.slice(2);
const number = parseInt(args);

function printNumber (number){
	if (isNaN(number)) {
		console.log('Not a number');
	} else {
		console.log('My number: ' + number);
	}
}

printNumber(number);
