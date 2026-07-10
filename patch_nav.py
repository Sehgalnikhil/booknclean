import glob
import re

files = ["index.html", "pricing.html", "how-it-works.html", "about.html", "services.html", "contact.html"]

hamburger_html = """
    <button class="nav-toggle" aria-label="Toggle navigation" onclick="document.body.classList.toggle('nav-open')">
      <svg viewBox="0 0 24 24"><path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/></svg>
    </button>
"""

overlay_html = '<div class="nav-overlay" onclick="document.body.classList.remove(\'nav-open\')"></div>'

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Check if already patched
    if 'class="nav-toggle"' in content:
        print(f"Skipping {f}, already patched.")
        continue

    # Insert toggle button right before <div class="nav-right">
    content = re.sub(r'(<div class="nav-right">)', hamburger_html + r'\1', content)
    
    # Insert overlay right before </nav> or after <nav>
    content = re.sub(r'(<nav class="nav">)', r'\1' + overlay_html, content)
    
    with open(f, 'w') as file:
        file.write(content)
    print(f"Patched {f}")
