import glob, re

files = glob.glob('*.html')
count = 0

pattern = re.compile(r"\s*/\* Auto-open bubble after 10s if not interacted \*/\s*var autoTimer;\s*if \(window\.innerWidth > 768\) \{\s*autoTimer = setTimeout\(function\(\)\{\s*bubble\.classList\.add\('open'\);\s*\}, 10000\);\s*\}", re.MULTILINE)
pattern2 = re.compile(r"\s*clearTimeout\(autoTimer\);", re.MULTILINE)

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    new_content, n = pattern.subn("", content)
    new_content, n2 = pattern2.subn("", new_content)
    
    if n > 0 or n2 > 0:
        count += 1
        with open(f, 'w') as file:
            file.write(new_content)

print(f"Updated WP popup in {count} files.")
