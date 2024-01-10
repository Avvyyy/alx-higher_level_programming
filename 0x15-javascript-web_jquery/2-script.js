//Script that updates color of DIV#red_header to #FF0000
$(document).ready(() =>{
	$('DIV#red_header').on('click', (event) => {
		$(event.currentTarget).css('color', '#FF0000');
	})
})
