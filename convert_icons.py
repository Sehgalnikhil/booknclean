from PIL import Image
import glob
import os

source_dir = "/Users/nikhilsehgal/.gemini/antigravity-ide/brain/845a4d23-a79e-4b49-a81c-b7f10e4c0817/"
dest_dir = "/Users/nikhilsehgal/bond/"

mapping = {
    'icon_1bed_1bath': 'img-1bed.webp',
    'icon_2bed_1bath': 'img-2bed.webp',
    'icon_2bed_2bath': 'img-2bed-2bath.webp',
    'icon_3bed_1bath': 'img-3bed-1bath.webp',
    'icon_3bed_2bath': 'img-3bed-2bath.webp',
    'icon_3bed_3bath': 'img-3bed-3bath.webp',
    'icon_4bed_2bath': 'img-4bed-2bath.webp',
    'icon_4bed_3bath': 'img-4bed-3bath.webp',
    'icon_5bed_2bath': 'img-5bed-2bath.webp',
    'icon_5bed_3bath': 'img-5bed-3bath.webp'
}

for prefix, dest_filename in mapping.items():
    pattern = os.path.join(source_dir, f"{prefix}*.png")
    matches = glob.glob(pattern)
    if matches:
        latest_file = max(matches, key=os.path.getctime)
        img = Image.open(latest_file)
        # convert to RGB if not already
        if img.mode != 'RGB':
            img = img.convert('RGB')
        dest_path = os.path.join(dest_dir, dest_filename)
        img.save(dest_path, 'WEBP', quality=85)
        print(f"Converted {latest_file} -> {dest_path}")
    else:
        print(f"No match found for {prefix}")
