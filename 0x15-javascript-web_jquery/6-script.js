//script that updates the text of the <header>
//element to New Header!!! when the user clicks on DIV#update_header

$(document).ready(() =>{
	$('DIV#update_header').on('click', () => {
		$('header').text("New Header!!!");
	})
})