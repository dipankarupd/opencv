import cv2
import numpy as np

# Function to calculate the centroid of a triangle
def calculate_centroid(points):
    x = int((points[0][0] + points[1][0] + points[2][0]) / 3)
    y = int((points[0][1] + points[1][1] + points[2][1]) / 3)
    return x, y

# Initialize the window and create an empty black image
image_size = (500, 500, 3)
image = np.zeros(image_size, dtype=np.uint8)

# Initial vertices of the triangle
triangle_vertices = np.array([[250, 100], [100, 400], [400, 400]], np.int32)

# Initial color of the triangle
triangle_color = (0, 255, 0)  # Green

while True:
    # Copy the original image to work on a fresh copy
    img = image.copy()

    # Draw the filled triangle on the image
    cv2.fillPoly(img, [triangle_vertices.reshape((-1, 1, 2))], color=triangle_color)

    # Calculate and draw the centroid
    centroid = calculate_centroid(triangle_vertices)
    cv2.circle(img, centroid, 5, (255, 255, 255), -1)
    # Display the image
    cv2.imshow('Triangle with Centroid', img)

    # Wait for a key press
    key = cv2.waitKey(0) & 0xFF

    # Check for key presses to change color or exit
    if key == ord('r'):
        # Change color to red
        triangle_color = (0, 0, 255)
    elif key == ord('g'):
        # Change color to green
        triangle_color = (0, 255, 0)
    elif key == ord('b'):
        # Change color to blue
        triangle_color = (255, 0, 0)
    elif key == 27:  # Esc key
        break

# Close all open windows
cv2.destroyAllWindows()
