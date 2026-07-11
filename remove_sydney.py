import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Text replacements
replacements = {
    "Perth, Melbourne, Brisbane, and Sydney": "Perth, Melbourne, and Brisbane",
    "Perth, Melbourne, Brisbane and Sydney": "Perth, Melbourne, and Brisbane",
    "Perth · Melbourne · Brisbane · Sydney": "Perth · Melbourne · Brisbane",
    "Perth, Melbourne, Brisbane & Sydney": "Perth, Melbourne & Brisbane",
    "Perth, Melbourne, Brisbane &amp; Sydney": "Perth, Melbourne &amp; Brisbane",
    "Perth, Melbourne, Brisbane, & Sydney": "Perth, Melbourne, & Brisbane",
}
for old, new in replacements.items():
    html = html.replace(old, new)

# 2. Remove area-card for Sydney
sydney_card_pattern = r'<div class="area-card"><div class="area-h">Sydney & Surrounds</div><div class="area-list">Parramatta[^<]+</div></div>\s*'
html = re.sub(sydney_card_pattern, '', html)

# 3. Remove PRICES['Sydney']
html = html.replace("PRICES['Sydney'] = PRICES['Brisbane'];", "")

# 4. Remove ADDON_PRICES['Sydney']
html = html.replace("ADDON_PRICES['Sydney'] = ADDON_PRICES['Brisbane'];", "")

# 5. Remove Sydney from city dropdown
sydney_option_pattern = r'<div class="suburb-option" data-val="Sydney">.*?</div>\s*'
html = re.sub(sydney_option_pattern, '', html, flags=re.DOTALL)

# 6. Remove from tz map
html = html.replace("'australia/sydney':'Sydney'", "")
# cleanup stray commas
html = html.replace(",''", "")
html = html.replace(",}", "}")

with open('index.html', 'w') as f:
    f.write(html)
