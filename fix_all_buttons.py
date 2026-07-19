#!/usr/bin/env python3
"""
fix_all_buttons.py
Applies all button/click/touch fixes to index.html and every suburb HTML page.

Fixes applied:
  1. normPhone regex bug — adds missing '' replacement string
  2. Double-event (click + touchend) — replaces with ghost-click-safe single handler
  3. prop-icon images — adds draggable="false" to prevent iOS drag-instead-of-tap
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ──────────────────────────────────────────────────────────────
# FIX 1: normPhone regex bug
#   Before: p=(p||'').replace(/[^\d+]/g);
#   After:  p=(p||'').replace(/[^\d+]/g,'');
# ──────────────────────────────────────────────────────────────
NORMPHONE_OLD = "p=(p||'').replace(/[^\\d+]/g);"
NORMPHONE_NEW = "p=(p||'').replace(/[^\\d+]/g,'');"

# ──────────────────────────────────────────────────────────────
# FIX 2: Replace dual click+touchend listener with ghost-safe handler.
# The old code registers BOTH 'click' and 'touchend' on document.
# On mobile, both fire for one tap, causing double execution.
# New approach: use only 'click' but suppress ghost clicks that
# arrive < 500ms after a touchend, using a lastTouchTime guard.
# Also adds e.preventDefault() on touchend for navigation buttons
# to stop the ghost click entirely.
# ──────────────────────────────────────────────────────────────

OLD_HANDLER_BLOCK = """  document.addEventListener('click', handleInteraction);
  document.addEventListener('touchend', handleInteraction, { passive: false });"""

NEW_HANDLER_BLOCK = """  // Mobile double-event fix: track last touch so ghost clicks are suppressed.
  // With touch-action:manipulation in CSS, the 300ms delay is already removed.
  // This guard prevents the ghost 'click' that fires 300ms after touchend.
  let _lastTouchEndTime = 0;

  document.addEventListener('touchend', function _touchEndTrack(e) {
    _lastTouchEndTime = Date.now();
    // Run the handler for touchend on nav/selection buttons immediately
    // so there is zero latency on mobile taps.
    const target = e.target;
    const btnNav = target.closest('[data-nxt], [data-prv]');
    const obtn1  = target.closest('.obtn[data-s="1"]');
    const obtn2  = target.closest('.obtn[data-s="2"]');
    const cbtnEl = target.closest('.cbtn');
    const adnEl  = target.closest('.adn:not(.adn-qty)');
    const aqtyEl = target.closest('.aqty-btn');

    if (btnNav || obtn1 || obtn2 || cbtnEl || adnEl || aqtyEl) {
      if (e.cancelable) e.preventDefault(); // blocks the ghost click
      handleInteraction(e);
    }
  }, { passive: false });

  document.addEventListener('click', function _clickGuard(e) {
    // Suppress ghost click that arrives within 500ms of a touchend
    if (Date.now() - _lastTouchEndTime < 500) return;
    handleInteraction(e);
  });"""

# ──────────────────────────────────────────────────────────────
# FIX 3: Add draggable="false" to prop-icon <img> tags
# ──────────────────────────────────────────────────────────────
def fix_prop_icons(html):
    """Add draggable='false' to all <img class='prop-icon'> elements."""
    # Match img tags with class prop-icon that don't already have draggable
    pattern = r'(<img\s[^>]*class="[^"]*prop-icon[^"]*"[^>]*?)(?<!draggable="false")(>)'
    def add_draggable(m):
        tag = m.group(1)
        if 'draggable=' not in tag:
            return tag + ' draggable="false"' + m.group(2)
        return m.group(0)
    return re.sub(pattern, add_draggable, html)

# ──────────────────────────────────────────────────────────────
# Apply all fixes to one HTML string
# ──────────────────────────────────────────────────────────────
def apply_fixes(html, filename):
    changes = []

    # Fix 1: normPhone
    if NORMPHONE_OLD in html:
        html = html.replace(NORMPHONE_OLD, NORMPHONE_NEW)
        changes.append("normPhone regex fixed")
    
    # Fix 2: Double-event handler
    if OLD_HANDLER_BLOCK in html:
        html = html.replace(OLD_HANDLER_BLOCK, NEW_HANDLER_BLOCK)
        changes.append("double-event handler replaced")

    # Fix 3: draggable="false" on prop-icon images
    before = html
    html = fix_prop_icons(html)
    if html != before:
        changes.append("draggable=false added to prop-icon images")

    return html, changes

# ──────────────────────────────────────────────────────────────
# Process all HTML files
# ──────────────────────────────────────────────────────────────
def main():
    html_files = (
        glob.glob(os.path.join(BASE_DIR, 'index.html')) +
        glob.glob(os.path.join(BASE_DIR, 'bond-cleaning-*.html'))
    )

    total = 0
    for filepath in sorted(html_files):
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        fixed, changes = apply_fixes(original, filename)
        
        if changes:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed)
            total += 1
            print(f"  OK {filename}: {', '.join(changes)}")
        else:
            print(f"  -- {filename}: no changes needed")

    print(f"\nDone. {total} file(s) updated.")

if __name__ == '__main__':
    main()
