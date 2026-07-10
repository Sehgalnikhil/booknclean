import glob
import os

def update_files():
    html_files = glob.glob('*.html')
    for filepath in html_files:
        with open(filepath, 'r') as f:
            content = f.read()
            
        new_content = content
        
        # Replace 800 with 3000
        new_content = new_content.replace('>800+<', '>3000+<')
        new_content = new_content.replace('800 bond cleans', '3000 bond cleans')
        new_content = new_content.replace('800+ completed', '3000+ completed')
        
        # Remove GST included
        new_content = new_content.replace('Fixed price. GST included.', 'Fixed price.')
        
        if content != new_content:
            with open(filepath, 'w') as f:
                f.write(new_content)

if __name__ == "__main__":
    update_files()
