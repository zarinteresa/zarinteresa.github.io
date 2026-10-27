(function () {
  var root = document.documentElement;

  // theme toggle
  var btn = document.getElementById('theme-toggle');
  var mq = window.matchMedia('(prefers-color-scheme: dark)');
  btn.addEventListener('click', function () {
    var dark = root.dataset.theme ? root.dataset.theme === 'dark' : mq.matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch (e) {}
  });

  // hash routing: #/home, #/courses
  var pages = document.querySelectorAll('.page');
  var links = document.querySelectorAll('[data-route]');
  function route() {
    var name = (location.hash.match(/^#\/(\w+)/) || [, 'home'])[1];
    if (!document.getElementById(name)) name = 'home';
    pages.forEach(function (p) { p.hidden = p.id !== name; });
    links.forEach(function (a) { a.classList.toggle('active', a.dataset.route === name); });
  }
  window.addEventListener('hashchange', route);
  route();

  // avatar rings follow the pointer
  var av = document.getElementById('avatar');
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var rings = {
      y: [av.querySelector('.ring--yellow'), -10, 4, 1],
      p: [av.querySelector('.ring--pink'), 10, -6, -1],
      b: [av.querySelector('.ring--blue'), 6, 8, 1]
    };
    function place(dx, dy) {
      for (var k in rings) {
        var r = rings[k];
        r[0].style.transform = 'translate(' + (r[1] + r[3] * dx) + 'px,' + (r[2] + r[3] * dy) + 'px)';
      }
    }
    av.addEventListener('pointermove', function (e) {
      var b = av.getBoundingClientRect();
      place(((e.clientX - b.left) / b.width - .5) * 24, ((e.clientY - b.top) / b.height - .5) * 24);
    });
    av.addEventListener('pointerleave', function () { place(0, 0); });
  }
})();
