var myLayout; // a var is required because this page utilizes: myLayout.allowOverflow() method
	$(document).ready(function () {
		myLayout = $('body').layout({
			west__size:					150
		,	west__spacing_closed:		20
		,	west__togglerLength_closed:	100
		,	west__togglerAlign_closed:	"top"
		,	west__togglerContent_closed:"M&amp;lt;BR>E&amp;lt;BR>N&amp;lt;BR>U"
		,	west__togglerTip_closed:	"Open &amp; Pin Menu"
		,	west__sliderTip:			"Slide Open Menu"
		,	west__slideTrigger_open:	"mouseover"
		,	center__maskContents:		true // IMPORTANT - enable iframe masking
		});
 	});