//Script that performs a GET request on a url

$(() => {
	$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", (body, res) => {
		$('DIV#character').text(body.name);
	})
})