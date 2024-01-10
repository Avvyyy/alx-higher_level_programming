//Script that performs a GET request on a URL
// Script iterates over a list of titles in teh URL and gets them

$(() => {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (body, res) => {
		$.each(body.results, (index, film) => {
			$('UL#list_movies').append(`<li>${film.title}</li>`);
		})
	})
})