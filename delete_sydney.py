import os

sydney_suburbs = [
  "Bondi", "Bondi Junction", "Surry Hills", "Newtown", "Parramatta", "Chatswood", 
  "Manly", "Cronulla", "Mosman", "Randwick", "Darlinghurst", "Paddington", 
  "Glebe", "Leichhardt", "Balmain", "Ryde", "Hornsby", "Liverpool", "Campbelltown", 
  "Penrith", "Blacktown", "Bankstown", "Hurstville", "Kogarah", "Strathfield", 
  "Auburn", "Burwood", "Eastwood", "Dee Why", "Brookvale"
]

for s in sydney_suburbs:
    filename = 'bond-cleaning-' + s.lower().replace(' ', '-') + '.html'
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
