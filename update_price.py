import re
import glob

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
    'Studio / Granny Flat': { without_carpet: 300, with_carpet: 330 },
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
    'Studio / Granny Flat': { without_carpet: 285.00, with_carpet: 313.50 },
    '1 Bedroom, 1 Bathroom': { without_carpet: 304.00, with_carpet: 332.50 },
    '2 Bedroom, 1 Bathroom': { without_carpet: 380.00, with_carpet: 427.50 },
    '2 Bedroom, 2 Bathroom': { without_carpet: 399.00, with_carpet: 456.00 },
    '3 Bedroom, 1 Bathroom': { without_carpet: 465.50, with_carpet: 494.00 },
    '3 Bedroom, 2 Bathroom': { without_carpet: 494.00, with_carpet: 551.00 },
    '3 Bedroom, 3 Bathroom': { without_carpet: 522.50, with_carpet: 579.50 },
    '4 Bedroom, 2 Bathroom': { without_carpet: 570.00, with_carpet: 636.50 },
    '4 Bedroom, 3 Bathroom': { without_carpet: 598.50, with_carpet: 665.00 },
    '5 Bedroom, 2 Bathroom': { without_carpet: 598.50, with_carpet: 665.00 },
    '5 Bedroom, 3 Bathroom': { without_carpet: 665.00, with_carpet: 712.50 }
  }
};
PRICES['Sydney'] = PRICES['Perth'];

const ADDON_PRICES = {
  'Melbourne': {
    'WIN': { 'Studio / Granny Flat': 40, '1 Bedroom, 1 Bathroom': 40, '2 Bedroom, 1 Bathroom': 70, '2 Bedroom, 2 Bathroom': 70, '3 Bedroom, 1 Bathroom': 90, '3 Bedroom, 2 Bathroom': 90, '3 Bedroom, 3 Bathroom': 90, '4 Bedroom, 2 Bathroom': 90, '4 Bedroom, 3 Bathroom': 90, '5 Bedroom, 2 Bathroom': 120, '5 Bedroom, 3 Bathroom': 120 },
    'WALL_SPOTS': { 'Studio / Granny Flat': 60, '1 Bedroom, 1 Bathroom': 60, '2 Bedroom, 1 Bathroom': 80, '2 Bedroom, 2 Bathroom': 80, '3 Bedroom, 1 Bathroom': 80, '3 Bedroom, 2 Bathroom': 80, '3 Bedroom, 3 Bathroom': 80, '4 Bedroom, 2 Bathroom': 100, '4 Bedroom, 3 Bathroom': 100, '5 Bedroom, 2 Bathroom': 120, '5 Bedroom, 3 Bathroom': 120 },
    'PEST': { 'Studio / Granny Flat': 120, '1 Bedroom, 1 Bathroom': 120, '2 Bedroom, 1 Bathroom': 140, '2 Bedroom, 2 Bathroom': 140, '3 Bedroom, 1 Bathroom': 150, '3 Bedroom, 2 Bathroom': 150, '3 Bedroom, 3 Bathroom': 150, '4 Bedroom, 2 Bathroom': 170, '4 Bedroom, 3 Bathroom': 170, '5 Bedroom, 2 Bathroom': 180, '5 Bedroom, 3 Bathroom': 180 }
  },
  'Brisbane': {
    'WIN': { 'Studio / Granny Flat': 50, '1 Bedroom, 1 Bathroom': 50, '2 Bedroom, 1 Bathroom': 80, '2 Bedroom, 2 Bathroom': 80, '3 Bedroom, 1 Bathroom': 110, '3 Bedroom, 2 Bathroom': 110, '3 Bedroom, 3 Bathroom': 110, '4 Bedroom, 2 Bathroom': 120, '4 Bedroom, 3 Bathroom': 120, '5 Bedroom, 2 Bathroom': 140, '5 Bedroom, 3 Bathroom': 140 },
    'WALL_SPOTS': { 'Studio / Granny Flat': 80, '1 Bedroom, 1 Bathroom': 80, '2 Bedroom, 1 Bathroom': 90, '2 Bedroom, 2 Bathroom': 90, '3 Bedroom, 1 Bathroom': 120, '3 Bedroom, 2 Bathroom': 120, '3 Bedroom, 3 Bathroom': 120, '4 Bedroom, 2 Bathroom': 150, '4 Bedroom, 3 Bathroom': 150, '5 Bedroom, 2 Bathroom': 180, '5 Bedroom, 3 Bathroom': 180 },
    'PEST': { 'Studio / Granny Flat': 120, '1 Bedroom, 1 Bathroom': 120, '2 Bedroom, 1 Bathroom': 140, '2 Bedroom, 2 Bathroom': 140, '3 Bedroom, 1 Bathroom': 150, '3 Bedroom, 2 Bathroom': 150, '3 Bedroom, 3 Bathroom': 150, '4 Bedroom, 2 Bathroom': 170, '4 Bedroom, 3 Bathroom': 170, '5 Bedroom, 2 Bathroom': 180, '5 Bedroom, 3 Bathroom': 180 }
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
  { v: 'Blind Cleaning (wipe)', i: '🪟', key: 'BLIND', p: 15, qty: true, hint: 'Slat-by-slat wiping of venetian or vertical blinds.' },
  { v: 'Shower Grout Mould Removal', i: '🧼', key: 'MOULD', p: 50, qty: true, hint: 'Removal of grout mould per mould spot.' },
  { v: 'Air Conditioner Filter Cleaning', i: '❄️', key: 'AC_FILTER', p: 20, qty: true, hint: 'Thorough cleaning of individual AC unit filters.' },
  { v: 'Wall Spots', i: '🧽', key: 'WALL_SPOTS', hint: 'Detail cleaning of wall scuffs and spots.' },
  { v: 'Pest / Flea Treatment', i: '🐜', key: 'PEST', hint: 'Professional interior pest & flea spray.' }
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
        
        if filename == 'pricing.html':
            print("Applying pricing.html specific static HTML updates...")
            new_content = new_content.replace('From $339', 'From $304') # Perth is 304 minimum
            new_content = new_content.replace('From $449', 'From $380')
            new_content = new_content.replace('From $549', 'From $465.50')
            new_content = new_content.replace('From $669', 'From $570')
            
            # DIY calculator total
            new_content = new_content.replace('Flat Rate From</span>\n            <span style="font-family:var(--ff-mono);font-size:24px;font-weight:800;color:var(--primary-ctr);">$339</span>',
                                              'Flat Rate From</span>\n            <span style="font-family:var(--ff-mono);font-size:24px;font-weight:800;color:var(--primary-ctr);">$310</span>')
            new_content = new_content.replace('Flat Rate From</span> <span style="font-family:var(--ff-mono);font-size:24px;font-weight:800;color:var(--primary-ctr);">$339</span>',
                                              'Flat Rate From</span> <span style="font-family:var(--ff-mono);font-size:24px;font-weight:800;color:var(--primary-ctr);">$310</span>')
            new_content = new_content.replace('const flatRate = 339;', 'const flatRate = 310;')
            
            # Additional Service Pricing list
            new_content = new_content.replace('<strong>External Window Cleaning</strong> <span>$70 to $150</span>',
                                              '<strong>External Window Cleaning</strong> <span>$40 to $140</span>')
            new_content = new_content.replace('<strong>Full Wall Wash</strong> <span>$25 per wall</span>',
                                              '<strong>Full Wall Wash</strong> <span>$20 per wall</span>')
            new_content = new_content.replace('<strong>Blind Cleaning (Wipe)</strong> <span>$20</span>',
                                              '<strong>Blind Cleaning (Wipe)</strong> <span>$15</span>')
            
            old_list_end = '      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Blind Cleaning (Wipe)</strong> <span>$15</span></li>\n    </ul>'
            new_list_end = ('      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Blind Cleaning (Wipe)</strong> <span>$15</span></li>\n'
                            '      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Shower Grout Mould Removal</strong> <span>$50 per spot</span></li>\n'
                            '      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Air Conditioner Filter Cleaning</strong> <span>$20 per filter</span></li>\n'
                            '      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Pest / Flea Treatment</strong> <span>$120 to $180</span></li>\n'
                            '      <li style="border-bottom: 1px solid rgba(0,0,0,0.05); padding: 8px 0; display: flex; justify-content: space-between;"><strong>Wall Spots</strong> <span>$60 to $180</span></li>\n'
                            '    </ul>')
            new_content = new_content.replace(old_list_end, new_list_end)

        if filename == 'how-it-works.html':
            print("Applying how-it-works.html specific updates...")
            new_content = new_content.replace('const flatRate = 339;', 'const flatRate = 310;')
            new_content = new_content.replace('color:var(--primary-ctr);">$339</span>', 'color:var(--primary-ctr);">$310</span>')

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")

if __name__ == '__main__':
    main()
