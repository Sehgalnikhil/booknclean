import os
import glob

def replace_extensions():
    files = glob.glob('*.html') + glob.glob('*.css')
    for filepath in files:
        with open(filepath, 'r') as f:
            content = f.read()
        
        # We need to be careful not to replace something that isn't an image name.
        # But for this simple project, replacing .png" and .jpg" should be safe.
        # Let's replace the specific image names we converted.
        images = [
            'img-1bed', 'oc-logo', 'img-3bed-1bath', 'img-2bed', 'img-studio', 
            'img-2bed-2bath', 'perth-hero', 'img-3bed-2bath', 'l', 
            'before-clean', 'after-clean', 'guarantee-bg'
        ]
        
        new_content = content
        for img in images:
            new_content = new_content.replace(f"{img}.png", f"{img}.webp")
            new_content = new_content.replace(f"{img}.jpg", f"{img}.webp")
            
        if content != new_content:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"Updated {filepath}")

if __name__ == "__main__":
    replace_extensions()
