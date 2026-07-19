import os

files = [f for f in os.listdir('.') if f.endswith('.html') and not f.startswith('bond-cleaning-')]
broken = []
for f in sorted(files):
    try:
        txt = open(f, encoding='utf-8').read()
        if 'nav-toggle' in txt and "onclick=\"document.body.classList.toggle('nav-open')" in txt:
            broken.append(f)
    except:
        pass

if broken:
    print('STILL BROKEN (double-toggle):')
    for b in broken:
        print(' -', b)
else:
    print('All clear - no double-toggle bugs found in main pages.')
