import re
import os

files = ['about.html', 'services.html', 'pricing.html', 'how-it-works.html', 'contact.html']

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # Find where <div class="nav-links"> starts
    # We want to replace everything from </a>\n    <div class="nav-links"> to the closing </div>
    # Actually, it's easier to match the whole nav-links div block.

    pattern = re.compile(r'(</a>\s*<div class="nav-links">)(.*?)(</div>\s*<button class="nav-toggle")', re.DOTALL)
    
    match = pattern.search(content)
    if match:
        links_inner = match.group(2)
        # add onclick to all links
        links_inner = re.sub(r'<a href="([^"]+)"( class="active")?>', r'<a href="\1"\2 onclick="document.body.classList.remove(\'nav-open\')">', links_inner)
        
        replacement = f'''</a>
    <div class="nav-overlay" onclick="document.body.classList.remove('nav-open')"></div>
    <div class="nav-links" id="navLinks">
      <button class="nav-close" onclick="document.body.classList.remove('nav-open')" aria-label="Close menu">✕</button>{links_inner}</div>
    <button class="nav-toggle"'''
        
        new_content = content[:match.start()] + replacement + content[match.end():]
        
        with open(file, 'w') as f:
            f.write(new_content)
        print(f"Fixed {file}")
    else:
        print(f"Could not find pattern in {file}")

