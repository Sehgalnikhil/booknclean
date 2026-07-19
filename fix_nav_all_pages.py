"""
fix_nav_all_pages.py
Replaces the old broken nav block in each internal page with the correct
shared nav structure that matches the fixed index.html.
- Removes double-toggle onclick
- Adds nav-overlay outside nav-inner
- Adds nav-close button inside nav-links
- Adds onclick close handlers on all nav links
- Sets correct 'active' class per page
"""

import re

# Map of filename → which page is 'active' in nav
PAGES = {
    'services.html':     'services.html',
    'how-it-works.html': 'how-it-works.html',
    'pricing.html':      'pricing.html',
    'about.html':        'about.html',
    'contact.html':      'contact.html',
}

# The correct nav block template (active_page gets the 'active' class)
def make_nav(active_page):
    def link(href, label):
        active = ' class="active"' if href == active_page else ''
        return f'      <a href="{href}"{active} onclick="document.body.classList.remove(\'nav-open\')">{label}</a>'

    return f"""<!-- ═══════════════════════════════════════════════════════════
     NAV
════════════════════════════════════════════════════════════ -->
  <nav>
    <!-- Full-screen overlay — must be OUTSIDE nav-inner so it is not clipped -->
    <div class="nav-overlay" onclick="document.body.classList.remove('nav-open')"></div>

    <div class="nav-inner">
      <!-- Logo -->
      <a class="nav-logo" href="/">
        <img src="oc-logo.webp" class="nav-logo-img" alt="Book &amp; Clean Logo">
        <div>
          <div class="nav-brand">Book &amp; Clean</div>
          <div class="nav-tagline">Bond Cleaning Experts</div>
        </div>
      </a>

      <!-- Desktop links + Mobile slide-in drawer -->
      <div class="nav-links" id="navLinks">
        <button class="nav-close" onclick="document.body.classList.remove('nav-open')" aria-label="Close menu">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
{link('index.html', 'Home')}
{link('services.html', 'Services')}
{link('how-it-works.html', 'How It Works')}
{link('pricing.html', 'Pricing')}
{link('about.html', 'About Us')}
{link('contact.html', 'Contact')}
      </div>

      <!-- Right side: Call + Get Quote (desktop) + hamburger toggle -->
      <div class="nav-right">
        <a href="tel:+61468230552" class="btn-call">
          <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          Call Now
        </a>
        <button class="btn-outline" onclick="document.getElementById('quote') ? document.getElementById('quote').scrollIntoView({{behavior:'smooth'}}) : window.location='index.html#quote'">Get Quote</button>
      </div>

      <!-- Hamburger toggle (mobile only) -->
      <button class="nav-toggle" aria-label="Toggle navigation">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
      </button>
    </div>
  </nav>"""

# Regex to match the entire nav block in each internal page
# Matches from the NAV comment (or from <nav> if no comment) through </nav>
NAV_PATTERN = re.compile(
    r'(?:<!--\s*[═]+\s*\n?\s*NAV\s*\n?\s*[═]+\s*-->)?\s*<nav>.*?</nav>',
    re.DOTALL
)

for filename, active in PAGES.items():
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        new_nav = make_nav(active)
        new_content, count = NAV_PATTERN.subn(new_nav, content, count=1)

        if count == 0:
            print(f"WARNING: No nav block found in {filename}")
        else:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed: {filename}")

    except FileNotFoundError:
        print(f"SKIPPED (not found): {filename}")
    except Exception as e:
        print(f"ERROR in {filename}: {e}")

print("Done.")
