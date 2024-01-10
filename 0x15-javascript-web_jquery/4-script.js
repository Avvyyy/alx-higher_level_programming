//script to toggle the class of a header between red and green

$('DIV#toggle_header').addClass('red');
$('DIV#toggle_header').on('click', (e) =>{
	$(e.currentTarget).toggleClass("green red");
})