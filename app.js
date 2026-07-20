// Mobile menu: aria-expanded, focus trap, ESC-to-close
const burger = document.querySelector('.burger');
const menu = document.querySelector('.mobile-menu');
if (burger && menu) {
  const links = menu.querySelectorAll('a');
  const setOpen = (open) => {
    document.body.classList.toggle('menu-open', open);
    burger.setAttribute('aria-expanded', String(open));
    if (open) { links[0].focus(); } else { burger.focus(); }
  };
  burger.setAttribute('aria-controls', 'mobile-menu');
  burger.setAttribute('aria-expanded', 'false');
  burger.addEventListener('click', () => setOpen(!document.body.classList.contains('menu-open')));
  links.forEach(a => a.addEventListener('click', () => document.body.classList.remove('menu-open')));
  document.addEventListener('keydown', (e) => {
    if (!document.body.classList.contains('menu-open')) return;
    if (e.key === 'Escape') { setOpen(false); }
    if (e.key === 'Tab') { // trap focus inside the open menu
      const f = [...links, burger];
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
      else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
    }
  });
}

// Scroll reveals (IntersectionObserver)
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
}, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// Services side-rail scrollspy
const rail = document.querySelector('.side-rail');
if (rail) {
  const anchors = [...rail.querySelectorAll('a[href^="#"]')];
  const targets = anchors.map(a => document.getElementById(a.hash.slice(1))).filter(Boolean);
  const spy = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        anchors.forEach(a => a.classList.toggle('active', a.hash === '#' + e.target.id));
      }
    });
  }, { rootMargin: '-30% 0px -60% 0px' });
  targets.forEach(t => spy.observe(t));
}
