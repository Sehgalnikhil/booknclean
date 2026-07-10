import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the hardcoded style with a class
new_content = content.replace('style="width:100px;height:auto;margin-bottom:8px;"', 'class="prop-icon"')

with open('index.html', 'w') as f:
    f.write(new_content)
