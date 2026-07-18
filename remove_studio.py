import os
import glob
import re

html_files = glob.glob('*.html')

button_pattern = re.compile(
    r'\s*<button class="obtn" data-s="1" data-v="Studio / Granny Flat">\s*<img src="img-studio\.webp"[^>]+>\s*<span class="on2">Studio / Granny Flat</span>\s*</button>',
    re.DOTALL
)

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content, num_subs = button_pattern.subn('', content)
    
    if num_subs > 0:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Removed from {filepath}")
