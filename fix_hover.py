import re

with open('style.css', 'r') as f:
    css = f.read()

# We need to wrap specific hover blocks in @media (hover: hover)
# Blocks we care about: .obtn:hover, .cbtn:hover, .adn:hover, .bb:hover, .bn:hover, .rst:hover, .aqty-btn:hover, .aqty-plus:hover
selectors = [
    r'\.obtn:hover', r'\.cbtn:hover', r'\.adn:hover', r'\.bb:hover', r'\.bn:hover', r'\.rst:hover', 
    r'\.aqty-btn:hover:not\(:disabled\)', r'\.aqty-plus:hover', r'\.nxt:hover'
]

for sel in selectors:
    # Match the selector and its entire block { ... }
    # Since some have multiple lines, we use a regex that matches until the closing brace
    pattern = r'(' + sel + r'\s*\{[^{}]*\})'
    
    # We use a function to replace it, adding @media (hover: hover) { ... }
    def repl(m):
        # Only wrap if it's not already wrapped! We can just replace the whole match
        # But wait, python regex doesn't know if it's already in a media query. 
        # But we know it isn't.
        return '@media (hover: hover) {\n  ' + m.group(1).replace('\n', '\n  ') + '\n}'
    
    css = re.sub(pattern, repl, css)

with open('style.css', 'w') as f:
    f.write(css)
