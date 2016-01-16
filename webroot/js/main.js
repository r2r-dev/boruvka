;(function(window) {
    function Menu(el, itemFunction) {
        this.el = el;

        // the menus (<ul>´s)
        this.menus = [].slice.call(this.el.querySelectorAll('.menu-item'));
        this.onItemClick = itemFunction;
        this._init();
    }

    Menu.prototype._init = function () {
        var self = this;

        this.menus.forEach(function (item) {
            item.querySelector('a').addEventListener('click', function (ev) {
                // add class current
                var current_link = self.el.querySelector('.menu-link--current');
                if (current_link) {
                    removeClass(self.el.querySelector('.menu-link--current'), 'menu-link--current');
                }
                addClass(ev.target, 'menu-link--current');

                var data_link = item.getAttribute('data-link');
                // callback
                self.onItemClick(ev, data_link);
            });
        });
    };
    window.Menu = Menu;
})(window);

(function() {
        ModalEffects();

		var menu_el = document.getElementById('menu');
        var menu = new Menu(menu_el, ajaxLoader);

		var gridWrapper = document.querySelector('.content');
        gridWrapper.addEventListener('tiles-loaded', function (e) {
            TileEffects();
            ModalEffects();
        }, false);

		function ajaxLoader(ev, data_link) {
			ev.preventDefault();
			gridWrapper.innerHTML = '';
			addClass(gridWrapper, 'content--loading');
			setTimeout(function() {
                var event = new Event('tiles-loaded');
				removeClass(gridWrapper, 'content--loading');
                ajaxGet(data_link, gridWrapper, event);
			}, 700);
		}
})();


/* Tile functions */
function replace(a, b) {
    fade(a);
    unfade(b);
}

function fade(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
            addClass(element, 'hidden');
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= op * 0.1;
    }, 10);
}

function unfade(element) {
    var op = 0.1;  // initial opacity
    var timer = setInterval(function () {
        if (op >= 1){
            clearInterval(timer);
            removeClass(element, 'hidden');
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += op * 0.1;
    }, 10);
}

function TileEffects() {
    [].slice.call(document.querySelectorAll('.tile')).forEach(function (el, i) {

        var front = el.querySelector('.front');
        var back = el.querySelector('.back');

        front.addEventListener('mouseover', function (ev) {
            replace(front, back);
            ev.stopPropagation();
        });

        //Safe mouseout, prevents from firing functions if event happens on children, not outside of actual element
        back.addEventListener('mouseout', function (ev) {
            var list = traverseChildren(back);
            var e = ev.toElement || ev.relatedTarget;
            if (!!~list.indexOf(e)) {
                return;
            }

            replace(back, front);

            ev.stopPropagation();
        });
    });
}

//quick and dirty DFS children traversal,
function traverseChildren(elem){
    var children = [];
    var q = [];
    q.push(elem);
    while (q.length > 0) {
      var elem = q.pop();
      children.push(elem);
      pushAll(elem.children);
    }
    function pushAll(elemArray){
      for(var i=0; i < elemArray.length; i++) {
        q.push(elemArray[i]);
      }
    }
    return children;
}


/* Modals */
function ModalEffects() {
    	var overlay = document.querySelector( '.modal-overlay' );
        var modal = document.querySelector('.modal');

		[].slice.call( document.querySelectorAll( '.modal-trigger' ) ).forEach( function( el, i ) {
            var data_link = el.getAttribute('data-link');

            // Use unique event ids, otherwise we are listening to all modals
            var event_guid = guid();
            var event = new Event(event_guid);

			function removeModal() {
				removeClass( modal, 'modal-show' );
			}

			function removeModalHandler() {
				removeModal();
			}

			el.addEventListener( 'click', function( ev ) {
                ajaxGet(data_link, modal, event);
				addClass(modal, 'modal-show');

                // Close modal if user clicked oudside of it
				overlay.removeEventListener( 'click', removeModalHandler );
				overlay.addEventListener( 'click', removeModalHandler );
			});

            modal.addEventListener(event_guid, function(ev) {
                var close = modal.querySelector('.modal-close' );
                var form = modal.querySelector('.modal-form');

                if (close != undefined) {
                    close.addEventListener('click', function (ev) {
                        ev.stopPropagation();
                        removeModalHandler();
                    });
                }

                if (form != undefined) {
                    // pass parent modal and event, allowing to control form after submission
                    // by dispatching the very same event
                    initializeForm(form, modal, event);
                }
            });
		});
}

function initializeForm(form, modal, event) {
    var submit = form.querySelector('.modal-submit');

    if (submit != undefined) {
        submit.addEventListener('click', function (ev) {
           ev.stopPropagation();
           submitForm(form, modal, event);
        });
    }
}

function submitForm(form, modal, event) {
    var data_link = form.getAttribute('data-link');
    var formData = new FormData();
    [].forEach.call(form.querySelectorAll('.input'), function( el ) {
        var input = el.childNodes[1];
        var name = input.id;
        var data;

        if (input.localName == 'input') {
            if (input.type == 'file' && input.files.length > 0) {
                data = input.files[0];
            } else {
                data = input.value;

            }
        } else if (input.localName == 'select') {
            data = input.options[input.selectedIndex].text;
        }

        if (data != undefined) {
            formData.append(name, data);
        }
    });
    ajaxPost(data_link, modal, formData, event);
}

/* Helper functions */
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

function guid() {
    function s4() {
        return Math.floor((1 + Math.random()) * 0x10000)
            .toString(16)
            .substring(1);
    }
    return 'i' + s4() + s4() + s4() + s4() + s4() + s4();
}

function ajaxGet(data_link, target, event) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            target.innerHTML = xhttp.responseText;
            if (event != undefined) {
                target.dispatchEvent(event);
            }
        }
    };
    xhttp.open("GET", data_link, true);
    xhttp.setRequestHeader("X-Requested-With",'XMLHttpRequest');
    xhttp.send();
}

function ajaxPost(data_link, target, form, event) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            target.innerHTML = xhttp.responseText;
            if (event != undefined) {
                target.dispatchEvent(event);
            }
        }
    };
    xhttp.open("POST", data_link, true);
    xhttp.setRequestHeader("X-Requested-With",'XMLHttpRequest');
    xhttp.send(form);
}