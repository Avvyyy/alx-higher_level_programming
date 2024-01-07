#!/usr/bin/node

let fs = require('fs');

function writeToFile(filepath, stringContent) {
	fs.writeFile(filepath, stringContent, "utf-8", (err) =>{
		if (err){
			console.error(err);
		}
	})
};

if (process.argv.length !== 4) {
	console.log("Usage: node scriptNmae.js <file_path> <content-to-write>");
} else {
	filepath = process.argv[2];
	stringContent = process.argv[3];
	writeToFile(filepath, stringContent);
}
