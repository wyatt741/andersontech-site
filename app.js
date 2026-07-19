// Mobile menu toggle
const burger = document.querySelector('.burger');
const closeMenu = () => document.body.classList.remove('menu-open');
if (burger) {
  burger.addEventListener('click', () => document.body.classList.toggle('menu-open'));
  document.querySelectorAll('.mobile-menu a').forEach(a => a.addEventListener('click', closeMenu));
}

// Scroll reveals via IntersectionObserver (no scroll listeners)
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  });
}, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
