#!/usr/bin/node

let request = require("request");
let url = process.argv[2];
let characterUrl = "https://swapi-api.alx-tools.com/api/people/18/";
let count = 0;

request(url, (err, res, body) => {
    if (err) {
        console.error(err);
        return;
    }

    const films = JSON.parse(body).results;

    // Loop through each film
    films.forEach(film => {
        // Check if the character "Wedge Antilles" is present in the characters array
        if (film.characters.includes(characterUrl)) {
            count += 1;
        }
    });

    // Print the final count
    console.log(count);
});
