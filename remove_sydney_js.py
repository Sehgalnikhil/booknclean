import re

with open('generate_seo_pages.js', 'r') as f:
    js = f.read()

# Remove the sydneySuburbs array
js = re.sub(r'const sydneySuburbs = \[.*?\];\n', '', js, flags=re.DOTALL)

# Remove the line spreading sydneySuburbs
js = re.sub(r'\s*\.\.\.sydneySuburbs\.map[^,]+,', '', js)

# Remove Sydney from the region conditional
js = js.replace("region === 'Sydney' ? 'NSW' : ", "")

with open('generate_seo_pages.js', 'w') as f:
    f.write(js)
