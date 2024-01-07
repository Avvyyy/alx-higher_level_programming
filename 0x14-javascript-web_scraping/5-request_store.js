#!/usr/bin/node

let fs = require("fs");
let request = require("request");
let url = process.argv[2];
let filePath = process.argv[3];

if (!url || !filePath) {
    console.log("Usage: node script.js <url> <filePath>");
} else {
    request(url, (err, res, body) => {
        if (err) {
            console.error(err);
        } else {
            // Move fs.writeFile inside the callback
            fs.writeFile(filePath, body, "utf-8", (err) => {
                if (err) {
                    console.error(err);
                }
	});
        }
    });
}

