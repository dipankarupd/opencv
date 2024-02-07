import cv2
import numpy as np

# Read an image from file
image = cv2.imread('input.png')

# Convert the image from BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert the image from RGB to Grayscale
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

# Display the original and converted images
cv2.imshow('Original Image', image)
cv2.imshow('RGB Image', rgb_image)
cv2.imshow('Grayscale Image', gray_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
