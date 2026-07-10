import cv2
import numpy as np

# Reload original - let me check the backup first
import os
if os.path.exists('perth-hero-orig.webp'):
    img = cv2.imread('perth-hero-orig.webp')
else:
    # We already overwrote it, so work with current but reset logic
    img = cv2.imread('perth-hero.webp')
    # The current one already has the maroon shirt, we need original
    print("WARNING: no backup found, working from potentially modified image")

print(f"Image shape: {img.shape}")

# Sample some pixels from typical shirt area (center of shirt region)
h, w = img.shape[:2]
# Sample mid region of the image (shirt area)
shirt_region = img[int(h*0.35):int(h*0.65), int(w*0.35):int(w*0.65)]
img_hsv_sr = cv2.cvtColor(shirt_region, cv2.COLOR_BGR2HSV)
print("Shirt region HSV stats:")
print(f"  H mean: {img_hsv_sr[:,:,0].mean():.1f}, range: {img_hsv_sr[:,:,0].min()}-{img_hsv_sr[:,:,0].max()}")
print(f"  S mean: {img_hsv_sr[:,:,1].mean():.1f}")
print(f"  V mean: {img_hsv_sr[:,:,2].mean():.1f}")
