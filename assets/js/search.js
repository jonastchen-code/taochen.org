// Filters the publication list on the Research page. The full list is visible without JavaScript.
(function () {
  var box = document.querySelector('.search');
  var q = document.getElementById('q');
  var status = document.getElementById('q-status');
  if (!box || !q) return;
  box.hidden = false;
  var papers = Array.prototype.slice.call(document.querySelectorAll('.paper'));
  var programs = Array.prototype.slice.call(document.querySelectorAll('.program'));
  function run() {
    var terms = q.value.toLowerCase().trim().split(/\s+/).filter(Boolean);
    var shown = 0;
    papers.forEach(function (p) {
      var text = p.getAttribute('data-search');
      var hit = terms.every(function (t) { return text.indexOf(t) !== -1; });
      p.hidden = !hit;
      if (hit) shown++;
    });
    programs.forEach(function (s) { s.hidden = !s.querySelector('.paper:not([hidden])'); });
    status.textContent = terms.length ? shown + ' of ' + papers.length + ' publications match.' : '';
  }
  q.addEventListener('input', run);
})();
