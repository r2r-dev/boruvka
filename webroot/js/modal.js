function hasClass(el, className) {
	if (el.classList)
		return el.classList.contains(className);
	else
		return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'))
}

function addClass(el, className) {
	if (el.classList)
		el.classList.add(className);
	else if (!hasClass(el, className)) el.className += " " + className
}

function removeClass(el, className) {
	if (el.classList)
		el.classList.remove(className);
	else if (hasClass(el, className)) {
		var reg = new RegExp('(\\s|^)' + className + '(\\s|$)');
		el.className=el.className.replace(reg, ' ')
	}
}

var ModalEffects = (function() {

	function init() {

		var overlay = document.querySelector( '.modal-overlay' );

		[].slice.call( document.querySelectorAll( '.modal-trigger' ) ).forEach( function( el, i ) {

			var modal = document.querySelector( '#' + el.getAttribute( 'data-modal' ) ),
				close = modal.querySelector( '.modal-close' );

			function removeModal() {
				removeClass( modal, 'modal-show' );
			}

			function removeModalHandler() {
				removeModal();
			}

			el.addEventListener( 'click', function( ev ) {
				addClass(modal, 'modal-show');
				overlay.removeEventListener( 'click', removeModalHandler );
				overlay.addEventListener( 'click', removeModalHandler );
			});

			close.addEventListener( 'click', function( ev ) {
				ev.stopPropagation();
				removeModalHandler();
			});

		} );

	}

	init();

})();