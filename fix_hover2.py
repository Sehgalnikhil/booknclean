import re

with open('style.css', 'r') as f:
    css = f.read()

# WebKit ignores @media (hover: hover) for the double-tap bug.
# We must rewrite the selectors to include a non-touch guard, e.g., 'body:not(.is-touch) .obtn:hover'
# However, the simplest foolproof way to fix this iOS Safari bug is to remove the :hover pseudo-class completely for these specific critical buttons, and use a .hover class triggered by JS for desktop, OR just let desktop not have complex hover states.
# Alternatively, since we only care about .obtn, .cbtn, .adn, .bn, .bb, .aqty-btn, we can just replace their :hover with :active!

selectors = [
    r'\.obtn:hover', r'\.cbtn:hover', r'\.adn:hover', r'\.bb:hover', r'\.bn:hover', r'\.rst:hover', 
    r'\.aqty-btn:hover', r'\.aqty-plus:hover', r'\.nxt:hover'
]

# We will just replace ':hover' with ':active' in the file for these buttons!
# Wait, ':active' triggers while the finger is down on mobile, providing great native touch feedback, AND it does NOT cause the double-tap bug!
# Let's replace the string directly in the css.

for sel in selectors:
    css = css.replace(sel.replace('\\', ''), sel.replace('\\', '').replace(':hover', ':active'))

with open('style.css', 'w') as f:
    f.write(css)

