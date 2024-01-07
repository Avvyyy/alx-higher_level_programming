#!/usr/bin/node

let request = require('request');
let id = process.argv[2];
let url;

if (!id)
	console.log("Usage: node script.js <id>");
else
	url = `https://swapi-api.alx-tools.com/api/films/${id}`;
	request(url, (err, res, body) => {
		if(err)
			console.error(err);
		else
			console.log(JSON.parse(body).title);
	})
