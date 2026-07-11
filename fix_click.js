const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const newScript = `
  let lastTouchTime = 0;
  
  const handleInteraction = (e) => {
    // Prevent duplicate firing between touchend and click
    if (e.type === 'touchend') {
      lastTouchTime = Date.now();
    } else if (e.type === 'click' && Date.now() - lastTouchTime < 500) {
      return; // Skip click if touchend just fired
    }
    
    // Handle Navigation Buttons
    const btnNav = e.target.closest('[data-nxt], [data-prv]');
    if (btnNav) {
      if (e.type === 'touchend' && e.cancelable) e.preventDefault(); // Prevent ghost click
      if (btnNav.hasAttribute('data-nxt')) { console.log("button tapped"); nxt(parseInt(btnNav.getAttribute('data-nxt'))); }
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
`;

html = html.replace(/const handleInteraction = \(e\) => \{[\s\S]*?const aminus = e\.target\.closest\('\.aqty-minus'\);[\s\S]*?return;\n    \}\n  \};/, newScript);

// We must also bind touchend
html = html.replace(/document\.addEventListener\('click', handleInteraction\);/, "document.addEventListener('click', handleInteraction);\n  document.addEventListener('touchend', handleInteraction, { passive: false });");

fs.writeFileSync('index.html', html);
