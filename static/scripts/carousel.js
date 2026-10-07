document.querySelectorAll('.carousel').forEach((carousel) => {
  const list = carousel.querySelector('ul');
  const slides = Array.from(list.children);
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let current = 0;

  // Buttons
  const makeButton = (cls, symbol, label) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = `carousel-btn ${cls}`;
    btn.textContent = symbol;
    btn.setAttribute('aria-label', label);
    return btn;
  };
  const prev = makeButton('carousel-btn--prev', '◄', 'Previous');
  const next = makeButton('carousel-btn--next', '►', 'Next');

  // Dots
  const dotsWrap = document.createElement('div');
  dotsWrap.className = 'carousel-dots';
  const dots = slides.map((slide, i) => {
    const dot = document.createElement('button');
    dot.type = 'button';
    dot.className = 'carousel-dot';
    dot.setAttribute('aria-label', slide.dataset.accname || `Item ${i + 1}`);
    dot.addEventListener('click', () => goTo(i));
    dotsWrap.appendChild(dot);
    return dot;
  });

  carousel.append(prev, next, dotsWrap);

  function goTo(index) {
    const i = Math.max(0, Math.min(slides.length - 1, index));
    slides[i].scrollIntoView({
      behavior: reduceMotion.matches ? 'auto' : 'smooth',
      inline: 'center',
      block: 'nearest', // don't scroll the page vertically
    });
  }

  function update() {
    current = Math.round(list.scrollLeft / list.clientWidth);
    current = Math.max(0, Math.min(slides.length - 1, current));
    prev.disabled = current === 0;
    next.disabled = current === slides.length - 1;
    dots.forEach((dot, i) => {
      if (i === current) dot.setAttribute('aria-current', 'true');
      else dot.removeAttribute('aria-current');
    });
  }

  // Throttle scroll updates to one per frame
  let ticking = false;
  list.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { update(); ticking = false; });
  }, { passive: true });

  window.addEventListener('resize', update);

  prev.addEventListener('click', () => goTo(current - 1));
  next.addEventListener('click', () => goTo(current + 1));

  // Arrow keys while the list is focused
  list.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft')  { e.preventDefault(); goTo(current - 1); }
    if (e.key === 'ArrowRight') { e.preventDefault(); goTo(current + 1); }
  });

  update();
});