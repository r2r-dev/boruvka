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
		var menu_el = document.getElementById('menu');
        var menu = new Menu(menu_el, ajaxLoader);

		var gridWrapper = document.querySelector('.content');

		function ajaxLoader(ev, data_link) {
			ev.preventDefault();
			gridWrapper.innerHTML = '';
			addClass(gridWrapper, 'content--loading');
			setTimeout(function() {
				removeClass(gridWrapper, 'content--loading');
				 ajaxGet(data_link, gridWrapper);
			}, 700);
		}

})();

function ajaxGet(data_link, target) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (xhttp.readyState == 4 && xhttp.status == 200) {
        target.innerHTML = xhttp.responseText;
    }
  };
  xhttp.open("GET", data_link, true);
  xhttp.send();
}

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