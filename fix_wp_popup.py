import glob, re

files = glob.glob('*.html')
count = 0

pattern = re.compile(r"(\s*/\* Auto-open bubble after 10s if not interacted \*/\s*)var autoTimer = setTimeout\(function\(\)\{\s*bubble\.classList\.add\('open'\);\s*\}, 10000\);", re.MULTILINE)

replacement = r"""\1var autoTimer;
  if (window.innerWidth > 768) {
    autoTimer = setTimeout(function(){
      bubble.classList.add('open');
    }, 10000);
  }"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content, n = pattern.subn(replacement, content)
    
    if n > 0:
        count += 1
        with open(f, 'w') as file:
            file.write(new_content)

print(f"Updated WP popup in {count} files.")
