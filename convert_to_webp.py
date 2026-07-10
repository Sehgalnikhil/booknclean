import os
import glob
from PIL import Image

def convert_to_webp():
    extensions = ['*.png', '*.jpg', '*.jpeg']
    files_to_convert = []
    
    for ext in extensions:
        files_to_convert.extend(glob.glob(ext))
        
    for file_path in files_to_convert:
        if file_path == 'oc-logo.png': # Small logo doesn't really need webp, but why not.
            pass
            
        base_name = os.path.splitext(file_path)[0]
        webp_path = f"{base_name}.webp"
        
        try:
            print(f"Converting {file_path} to {webp_path}...")
            # Open the image
            with Image.open(file_path) as img:
                # Convert RGBA to RGB for JPEG if needed, but webp supports RGBA
                img.save(webp_path, 'webp', quality=85, method=6)
            
            # Print file size savings
            old_size = os.path.getsize(file_path)
            new_size = os.path.getsize(webp_path)
            print(f"  Saved {(old_size - new_size) / 1024:.1f} KB")
        except Exception as e:
            print(f"Error converting {file_path}: {e}")

if __name__ == "__main__":
    convert_to_webp()
