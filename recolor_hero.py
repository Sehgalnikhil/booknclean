import cv2
import numpy as np

# Load image
img = cv2.imread('perth-hero.webp')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Target coral color: #E8705A → BGR = (90, 112, 232)
coral_bgr = np.array([90, 112, 232], dtype=np.uint8)
coral_h, coral_s, coral_v = cv2.cvtColor(coral_bgr.reshape(1,1,3), cv2.COLOR_BGR2HSV)[0][0]
print(f"Coral HSV: H={coral_h}, S={coral_s}, V={coral_v}")

# Mask: dark green shirt (hue ~60-85, high sat, medium-low val)
mask_shirt = cv2.inRange(img_hsv,
    np.array([45, 80, 20]),    # lower: H=45, S=80, V=20
    np.array([90, 255, 130])   # upper: H=90, S=255, V=130
)

# Mask: light green gloves/cloth (hue ~55-90, lower sat, higher val)
mask_gloves = cv2.inRange(img_hsv,
    np.array([50, 30, 80]),    # lower
    np.array([100, 200, 220])  # upper
)

# Combine masks
mask_all = cv2.bitwise_or(mask_shirt, mask_gloves)

# Slightly dilate to catch edges
kernel = np.ones((3,3), np.uint8)
mask_all = cv2.dilate(mask_all, kernel, iterations=1)
mask_all = cv2.GaussianBlur(mask_all, (5, 5), 0)

# Work in HSV: shift hue to coral and adjust saturation/value
result_hsv = img_hsv.copy()

# For the shirt (dark green → dark coral)
shirt_mask = mask_shirt > 50
result_hsv[shirt_mask, 0] = coral_h          # Set hue to coral
result_hsv[shirt_mask, 1] = np.clip(result_hsv[shirt_mask, 1].astype(int) + 20, 0, 255)  # Boost sat slightly

# For the gloves/cloth (light green → light coral)
gloves_only = (mask_gloves > 50) & ~shirt_mask
result_hsv[gloves_only, 0] = coral_h         # Set hue to coral
result_hsv[gloves_only, 1] = np.clip(result_hsv[gloves_only, 1].astype(int) + 10, 0, 255)

# Convert back to BGR
result_bgr = cv2.cvtColor(result_hsv, cv2.COLOR_HSV2BGR)

# Blend: use alpha for soft transition at mask edges
alpha = mask_all.astype(float) / 255.0
for c in range(3):
    result_bgr[:,:,c] = (alpha * result_bgr[:,:,c] + (1 - alpha) * img[:,:,c]).astype(np.uint8)

# Save
cv2.imwrite('perth-hero.webp', result_bgr, [cv2.IMWRITE_WEBP_QUALITY, 92])
print("Saved perth-hero.webp with recolored shirt and gloves!")
