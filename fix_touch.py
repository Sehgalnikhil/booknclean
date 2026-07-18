import glob, re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Remove touchstart listener
    content = re.sub(r"\s*document\.addEventListener\('touchstart'[\s\S]*?\{ passive: true \}\);", "", content)
    
    # Remove touchend listener
    content = re.sub(r"\s*document\.addEventListener\('touchend', handleInteraction, \{ passive: false \}\);", "", content)
    
    with open(f, 'w') as file:
        file.write(content)

print(f"Fixed {len(files)} HTML files.")
