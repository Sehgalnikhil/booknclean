import re

with open('style.css', 'r') as f:
    css = f.read()

# We want to replace :active with :hover inside @media (hover: hover) blocks for the specific buttons.
# Let's find all @media (hover: hover) blocks
def replace_active(match):
    block = match.group(0)
    # Replace the specific classes
    classes = ['.obtn', '.cbtn', '.adn', '.bb', '.bn', '.rst', '.aqty-btn', '.aqty-plus', '.nxt']
    for cls in classes:
        block = block.replace(cls + ':active', cls + ':hover')
    return block

css = re.sub(r'@media \(hover: hover\) \{.*?^\}', replace_active, css, flags=re.DOTALL | re.MULTILINE)

with open('style.css', 'w') as f:
    f.write(css)
