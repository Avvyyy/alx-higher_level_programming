//Script that adds the class, red, to DIV#red_header using JQuery

$(document).ready(() =>{
	$('DIV#red_header').on('click', (event) => {
		$(event.currentTarget).addClass('red');
	})
})
