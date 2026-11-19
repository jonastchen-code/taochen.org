// Counts clicks on paper PDFs and on DOI, SSRN and journal links, so we can see which papers
// visitors open. Uses GoatCounter (no cookies, no personal data). Does nothing if it is blocked.
(function () {
  function kind(a) {
    var h = a.getAttribute("href") || "";
    if (/\.pdf($|[?#])/i.test(h)) return "pdf";
    if (/^https?:\/\/(dx\.)?doi\.org\//i.test(h)) return "doi";
    if (/ssrn\.com/i.test(h)) return "ssrn";
    if (/scholar\.google\./i.test(h)) return null;
    if (/^https?:\/\//i.test(h) && a.host !== location.host) return "out";
    return null;
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var k = kind(a);
    if (!k || !window.goatcounter || !window.goatcounter.count) return;
    var page = location.pathname.replace(/^\/research\//, "").replace(/\/$/, "") || "home";
    var target = k === "pdf" ? a.pathname.split("/").pop() : a.host + a.pathname;
    window.goatcounter.count({ path: k + ": " + page + " -> " + target, title: (a.textContent || "").trim().slice(0, 120), event: true });
  }, true);
})();
