const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

// We will remove the previous handleInteraction and replace it with a robust one.
const regex = /let lastTouchTime = 0;[\s\S]*?document\.addEventListener\('touchend', handleInteraction, \{ passive: false \}\);/;

const newScript = `let lastTouchTime = 0;
  let touchStartX = 0;
  let touchStartY = 0;

  document.addEventListener('touchstart', (e) => {
    touchStartX = e.touches[0].clientX;
    touchStartY = e.touches[0].clientY;
  }, { passive: true });

  const handleInteraction = (e) => {
    if (e.type === 'touchend') {
      const touchEndX = e.changedTouches[0].clientX;
      const touchEndY = e.changedTouches[0].clientY;
      // If the user moved their finger more than 10px, it was a scroll, NOT a tap.
      if (Math.abs(touchEndX - touchStartX) > 10 || Math.abs(touchEndY - touchStartY) > 10) {
        return; // Ignore this touchend, let native scroll happen
      }
      lastTouchTime = Date.now();
    } else if (e.type === 'click' && Date.now() - lastTouchTime < 500) {
      return; // Skip ghost click
    }

    // Handle Navigation Buttons
    const btnNav = e.target.closest('[data-nxt], [data-prv]');
    if (btnNav) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      if (btnNav.hasAttribute('data-nxt')) nxt(parseInt(btnNav.getAttribute('data-nxt')));
      else if (btnNav.hasAttribute('data-prv')) prv(parseInt(btnNav.getAttribute('data-prv')));
      return;
    }
    // Handle Property Size / Type Buttons
    const obtn1 = e.target.closest('.obtn[data-s="1"]');
    if (obtn1) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      document.querySelectorAll('.obtn[data-s="1"]').forEach(x=>x.classList.remove('sel'));
      obtn1.classList.add('sel');S.ps=obtn1.dataset.v;S.ads=[];S.at=0;
      if(typeof updateStickySummary==='function') updateStickySummary();
      return;
    }
    const obtn2 = e.target.closest('.obtn[data-s="2"]');
    if (obtn2) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      document.querySelectorAll('.obtn[data-s="2"]').forEach(x=>x.classList.remove('sel'));
      obtn2.classList.add('sel');S.pt=obtn2.dataset.v;S.pm=parseFloat(obtn2.dataset.m);
      if(typeof updateStickySummary==='function') updateStickySummary();
      return;
    }
    const cbtn = e.target.closest('.cbtn');
    if (cbtn) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      document.querySelectorAll('.cbtn').forEach(x=>x.classList.remove('sel'));
      cbtn.classList.add('sel');S.ca=cbtn.dataset.v;
      if(typeof updateStickySummary==='function') updateStickySummary();
      return;
    }
    const adn = e.target.closest('.adn');
    if (adn) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      adn.classList.toggle('sel');
      buildExtras();
      return;
    }
    const aplus = e.target.closest('.aqty-plus');
    if (aplus) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      const p = aplus.closest('.aqty-wrap');
      const s = p.querySelector('.aqty-span');
      let v = parseInt(s.textContent);
      v++;
      s.textContent = v;
      p.querySelector('.aqty-minus').disabled = false;
      buildExtras();
      return;
    }
    const aminus = e.target.closest('.aqty-minus');
    if (aminus) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault();
      if(aminus.disabled) return;
      const p = aminus.closest('.aqty-wrap');
      const s = p.querySelector('.aqty-span');
      let v = parseInt(s.textContent);
      if(v > 0) {
        v--;
        s.textContent = v;
        if(v === 0) aminus.disabled = true;
        buildExtras();
      }
      return;
    }
  };

  document.addEventListener('click', handleInteraction);
  document.addEventListener('touchend', handleInteraction, { passive: false });`;

html = html.replace(regex, newScript);
fs.writeFileSync('index.html', html);
