//Script to perform a GET request on a URL
//The script will be imported from the head tag

$(document).ready(
$(() => {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (body, res) => {
		$('DIV#hello').text(body.hello);
	})
})
)