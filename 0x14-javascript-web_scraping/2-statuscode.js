#!/usr/bin/node

const request = require('request');

getRequest = (url) => {
	request(url, (err, res) => {
		if (err)
			console.error(err);
		else
			//Printing the status ocde
			console.log("code: " + res.statusCode);
	})
}

if (process.argv.length !== 3)
	console.log("Usage: node script.js <url>");
else {
	let url = process.argv[2];
	getRequest(url);
}
