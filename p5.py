import cv2
import numpy as np

# Reading the input image
img = cv2.imread('input.png', 0)

# Check if the image is read successfully
if img is None:
    print("Error: Unable to read the image.")
    exit()

# Taking a matrix of size 5 as the kernel
kernel = np.ones((3, 3), np.uint8)

# The first parameter is the original image,
# kernel is the matrix with which the image is
# convolved, and the third parameter is the number
# of iterations, which will determine how much
# you want to erode/dilate a given image.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

# Wait for a key press and close all windows on key press
cv2.waitKey(0)
cv2.destroyAllWindows()
