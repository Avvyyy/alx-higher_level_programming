#!/usr/bin/node

const fs = require('fs');

function readAndPrintFileContent(filePath) {
    fs.readFile(filePath, 'utf-8', (err, content) => {
        if (err) {
            console.error(`An error occurred: ${err.message}`);
        } else {
            console.log(content);
        }
    });
}

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
    console.log('Usage: node script.js <file_path>');
} else {
    const filePath = process.argv[2];
    readAndPrintFileContent(filePath);
}

