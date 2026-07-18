import re

def main():
    new_js_block = """const PRICES = {
  'Melbourne': {
    'Studio / Granny Flat': { without_carpet: 190, with_carpet: 210 },
    '1 Bedroom, 1 Bathroom': { without_carpet: 200, with_carpet: 220 },
    '2 Bedroom, 1 Bathroom': { without_carpet: 250, with_carpet: 280 },
    '2 Bedroom, 2 Bathroom': { without_carpet: 280, with_carpet: 320 },
    '3 Bedroom, 1 Bathroom': { without_carpet: 340, with_carpet: 350 },
    '3 Bedroom, 2 Bathroom': { without_carpet: 360, with_carpet: 380 },
    '3 Bedroom, 3 Bathroom': { without_carpet: 390, with_carpet: 410 },
    '4 Bedroom, 2 Bathroom': { without_carpet: 400, with_carpet: 420 },
    '4 Bedroom, 3 Bathroom': { without_carpet: 450, with_carpet: 480 },
    '5 Bedroom, 2 Bathroom': { without_carpet: 450, with_carpet: 480 },
    '5 Bedroom, 3 Bathroom': { without_carpet: 480, with_carpet: 500 }
  },
  'Brisbane': {
    'Studio / Granny Flat': { without_carpet: 310, with_carpet: 350 },
    '1 Bedroom, 1 Bathroom': { without_carpet: 320, with_carpet: 350 },
    '2 Bedroom, 1 Bathroom': { without_carpet: 400, with_carpet: 450 },
    '2 Bedroom, 2 Bathroom': { without_carpet: 420, with_carpet: 480 },
    '3 Bedroom, 1 Bathroom': { without_carpet: 490, with_carpet: 520 },
    '3 Bedroom, 2 Bathroom': { without_carpet: 520, with_carpet: 580 },
    '3 Bedroom, 3 Bathroom': { without_carpet: 550, with_carpet: 610 },
    '4 Bedroom, 2 Bathroom': { without_carpet: 600, with_carpet: 670 },
    '4 Bedroom, 3 Bathroom': { without_carpet: 630, with_carpet: 700 },
    '5 Bedroom, 2 Bathroom': { without_carpet: 630, with_carpet: 700 },
    '5 Bedroom, 3 Bathroom': { without_carpet: 700, with_carpet: 750 }
  },
  'Perth': {
    'Studio / Granny Flat': { without_carpet: 295, with_carpet: 325 },
    '1 Bedroom, 1 Bathroom': { without_carpet: 304, with_carpet: 332.5 },
    '2 Bedroom, 1 Bathroom': { without_carpet: 380, with_carpet: 427.5 },
    '2 Bedroom, 2 Bathroom': { without_carpet: 399, with_carpet: 456 },
    '3 Bedroom, 1 Bathroom': { without_carpet: 465.5, with_carpet: 494 },
    '3 Bedroom, 2 Bathroom': { without_carpet: 494, with_carpet: 551 },
    '3 Bedroom, 3 Bathroom': { without_carpet: 522.5, with_carpet: 579.5 },
    '4 Bedroom, 2 Bathroom': { without_carpet: 570, with_carpet: 636.5 },
    '4 Bedroom, 3 Bathroom': { without_carpet: 598.5, with_carpet: 665 },
    '5 Bedroom, 2 Bathroom': { without_carpet: 598.5, with_carpet: 665 },
    '5 Bedroom, 3 Bathroom': { without_carpet: 665, with_carpet: 712.5 }
  }
};
PRICES['Sydney'] = PRICES['Perth'];

const ADDON_PRICES = {
  'Melbourne': {
    'WIN': { 'Studio / Granny Flat': 40, '1 Bedroom, 1 Bathroom': 40, '2 Bedroom, 1 Bathroom': 70, '2 Bedroom, 2 Bathroom': 70, '3 Bedroom, 1 Bathroom': 90, '3 Bedroom, 2 Bathroom': 90, '3 Bedroom, 3 Bathroom': 90, '4 Bedroom, 2 Bathroom': 90, '4 Bedroom, 3 Bathroom': 90, '5 Bedroom, 2 Bathroom': 120, '5 Bedroom, 3 Bathroom': 120 }
  },
  'Brisbane': {
    'WIN': { 'Studio / Granny Flat': 50, '1 Bedroom, 1 Bathroom': 50, '2 Bedroom, 1 Bathroom': 80, '2 Bedroom, 2 Bathroom': 80, '3 Bedroom, 1 Bathroom': 110, '3 Bedroom, 2 Bathroom': 110, '3 Bedroom, 3 Bathroom': 110, '4 Bedroom, 2 Bathroom': 120, '4 Bedroom, 3 Bathroom': 120, '5 Bedroom, 2 Bathroom': 140, '5 Bedroom, 3 Bathroom': 140 }
  }
};
ADDON_PRICES['Perth'] = ADDON_PRICES['Brisbane'];
ADDON_PRICES['Sydney'] = ADDON_PRICES['Perth'];

const ADDEF = [
  { v: 'External Window Cleaning', i: '🪟', key: 'WIN', hint: 'Exterior glass on the ground floor, external sills, and tracks.' },
  { v: 'Stair Carpet Steam Cleaning', i: '🪜', key: 'STAIRS', p: 40, qty: true, hint: 'Professional steam cleaning per staircase.' },
  { v: 'Garage Cleaning', i: '🚗', key: 'GARAGE', p: 50, qty: true, hint: 'Sweeping and removing cobwebs from garage space.' },
  { v: 'Study / Theatre Room', i: '🎬', key: 'STUDY', p: 25, qty: true, hint: 'Cleaning of additional study or theatre rooms.' },
  { v: 'Extra Living Room', i: '🛋️', key: 'LIVING', p: 30, qty: true, hint: 'Cleaning of additional living spaces.' },
  { v: 'Balcony Cleaning', i: '🏙️', key: 'BALCONY', p: 40, qty: true, hint: 'Sweeping and mopping of balcony floors.' },
  { v: 'Full Wall Wash (Per Wall)', i: '🧽', key: 'WALL_WASH', p: 20, qty: true, hint: 'Full wash of individual walls to remove heavy marks.' },
  { v: 'Blind Cleaning (wipe)', i: '🪟', key: 'BLIND', p: 15, qty: true, hint: 'Slat-by-slat wiping of venetian or vertical blinds.' }
];"""

    pattern = re.compile(r'(const|let)\s+PRICES\s*=\s*\{.*?(const|let)\s+ADDEF\s*=\s*\[.*?\n\s*\]\s*;?', re.DOTALL)

    target_files = ['index.html', 'pricing.html', 'services.html', 'how-it-works.html']
    
    for filename in target_files:
        print(f"Updating JS blocks in {filename}...")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        matches = list(pattern.finditer(content))
        if not matches:
            print(f"WARNING: Could not find PRICES/ADDEF pattern in {filename}")
            continue
        
        new_content = pattern.sub(new_js_block, content)
        
        if filename == 'how-it-works.html':
            print("Applying how-it-works.html DIY calculator specific updates...")
            new_content = new_content.replace('const flatRate = 339;', 'const flatRate = 310;')
            new_content = new_content.replace('color:var(--primary-ctr);">$339</span>', 'color:var(--primary-ctr);">$310</span>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")

if __name__ == '__main__':
    main()
