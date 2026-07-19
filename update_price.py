import glob
import os

def update_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        with open(filepath, 'r') as f:
            content = f.read()
            
        new_content = content
        
        # Replace the price for the wall wash addon
        old_str = "key:'WALL_WASH',p:25"
        new_str = "key:'WALL_WASH',p:15"
        
        old_str2 = "key: 'WALL_WASH', p: 25"
        new_str2 = "key: 'WALL_WASH', p: 15"
        
        new_content = new_content.replace(old_str, new_str)
        new_content = new_content.replace(old_str2, new_str2)
        
        if content != new_content:
            with open(filepath, 'w') as f:
                f.write(new_content)

if __name__ == "__main__":
    update_files()
