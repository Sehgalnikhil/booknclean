import cv2
import numpy as np

img = cv2.imread('/Users/nikhilsehgal/.gemini/antigravity-ide/brain/d2c747c4-230f-4f35-92e1-11c054b2a628/media__1783664346138.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
kernel = np.ones((3,3), np.uint8)
edges = cv2.dilate(edges, kernel, iterations=1)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if 50 < w < 250 and 50 < h < 200:
        if 1.0 < w/h < 2.0:
            boxes.append((x, y, w, h))

final_boxes = []
for b in boxes:
    overlap = False
    for fb in final_boxes:
        x1 = max(b[0], fb[0])
        y1 = max(b[1], fb[1])
        x2 = min(b[0]+b[2], fb[0]+fb[2])
        y2 = min(b[1]+b[3], fb[1]+fb[3])
        if x1 < x2 and y1 < y2:
            overlap = True
            break
    if not overlap:
        final_boxes.append(b)

final_boxes.sort(key=lambda b: b[1])

rows = []
curr_row = []
last_y = -1
for b in final_boxes:
    if last_y == -1 or abs(b[1] - last_y) < 30:
        curr_row.append(b)
        last_y = b[1]
    else:
        rows.append(sorted(curr_row, key=lambda x: x[0]))
        curr_row = [b]
        last_y = b[1]
if curr_row:
    rows.append(sorted(curr_row, key=lambda x: x[0]))

sorted_boxes = []
for r in rows:
    sorted_boxes.extend(r)

names = [
    "img-studio.webp",
    "img-1bed.webp",
    "img-2bed.webp",
    "img-2bed-2bath.webp",
    "img-3bed-1bath.webp",
    "img-3bed-2bath.webp",
    "img-3bed-3bath.webp",
    "img-4bed-2bath.webp",
    "img-4bed-3bath.webp",
    "img-5bed-2bath.webp",
    "img-5bed-3bath.webp"
]

for i, (x, y, w, h) in enumerate(sorted_boxes):
    if i < len(names):
        # The detected box might be the inner image. Let's not add padding.
        crop = img[y:y+h, x:x+w]
        cv2.imwrite(names[i], crop)
        print(f"Saved {names[i]} size {w}x{h}")

