import cv2
import numpy as np
import random


def create_blank(width, height, rgb_color=(0, 0, 0)):
    """Create new image(numpy array) filled with certain color in RGB"""
    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image


# Create new blank 300x300 red image
width1, height1 = 60, 60

count = 50
for num in range(count):
    color = (random.choice(range(0,255)), random.choice(range(0,255)), random.choice(range(0,255)))
    image = create_blank(width1, height1, rgb_color=color)
    cv2.imwrite(f'./profile_images/dummy-avatar{num}.jpg', image)
    cv2.imwrite(f'./items/dummy-item{num}.jpg', image)
    