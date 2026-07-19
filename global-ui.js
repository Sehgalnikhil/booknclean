document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky & Shrinking Navigation
  const nav = document.querySelector('nav');

  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        nav.classList.add('nav-scrolled');
      } else {
        nav.classList.remove('nav-scrolled');
      }
    }, { passive: true });
  }

  // 2. Scroll-to-Top Button
  const scrollTopBtn = document.createElement('button');
  scrollTopBtn.id = 'scrollTopBtn';
  scrollTopBtn.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>';
  scrollTopBtn.setAttribute('aria-label', 'Scroll to top');
  document.body.appendChild(scrollTopBtn);

  // Show/Hide logic
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      scrollTopBtn.classList.add('show');
    } else {
      scrollTopBtn.classList.remove('show');
    }
  }, { passive: true });

  // Scroll to top on click
  scrollTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  // 3. Universal Mobile Nav: Inject .nav-overlay and .nav-close if missing
  //    This keeps inner pages and suburb landing pages fully consistent
  //    without editing 90+ generated HTML files individually.
  const navLinks = document.querySelector('.nav-links');

  if (navLinks) {
    // Inject dark overlay behind menu if not already in DOM
    let overlay = document.querySelector('.nav-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'nav-overlay';
      document.body.appendChild(overlay);
    }
    overlay.addEventListener('click', () => {
      document.body.classList.remove('nav-open');
    });

    // Inject close (✕) button inside nav-links panel if not already there
    let closeBtn = navLinks.querySelector('.nav-close');
    if (!closeBtn) {
      closeBtn = document.createElement('button');
      closeBtn.className = 'nav-close';
      closeBtn.setAttribute('aria-label', 'Close menu');
      closeBtn.innerHTML = '&#x2715;';
      navLinks.insertBefore(closeBtn, navLinks.firstChild);
    }
    closeBtn.addEventListener('click', () => {
      document.body.classList.remove('nav-open');
    });

    // Close menu when any nav link is tapped (important for mobile anchor links)
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        document.body.classList.remove('nav-open');
      });
    });
  }

  // 4. Hamburger toggle button — ensure it works on all pages
  const navToggle = document.querySelector('.nav-toggle');
  if (navToggle) {
    navToggle.addEventListener('click', () => {
      document.body.classList.toggle('nav-open');
    });
  }
});

