import glob, re

files = glob.glob('*.html')
count_replaced = 0
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    pattern = r'performance\.mark\("nxt-start"\);[\s\S]*?if\s*\(\s*step\s*===\s*3\s*\)\s*buildAds\(\);'
    replacement = r'''performance.mark("nxt-start");
    
    if(step===5){
      S.dt=document.getElementById('idate').value;
      S.addr=document.getElementById('iaddr').value.trim();
      S.sub=document.getElementById('isub').value.trim();
      if(S.sub){S.city=S.sub;}
    }

    if(step===3) buildAds();'''
    
    new_content, count = re.subn(pattern, replacement, content)
    if count > 0:
        count_replaced += 1
        with open(f, 'w') as file:
            file.write(new_content)

print(f"Replaced validation in {count_replaced} files.")
