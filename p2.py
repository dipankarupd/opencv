from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import sys
import cv2

# Function to draw a wireframe cube
def draw_wireframe_cube():
    glutWireCube(1)

# Function to display the scene with a wireframe cube
def display_wireframe_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

    glColor3f(1, 0, 0)  # Set color to red
    glTranslatef(-1.5, 0, 0)  # Translate to the left
    draw_wireframe_cube()

    glutSwapBuffers()

# Initialize OpenGL parameters
def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

# Function to handle window resizing
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Capture OpenGL rendering to an OpenCV image
def capture_opengl_to_opencv(width, height):
    glReadBuffer(GL_FRONT)
    pixels = glReadPixels(0, 0, width, height, GL_BGR, GL_UNSIGNED_BYTE)
    image = np.frombuffer(pixels, dtype=np.uint8)
    image = image.reshape((height, width, 3))
    return cv2.flip(image, 0)

# Main function for wireframe cube
def main_wireframe_cube():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Wireframe Cube using OpenGL")

    glutDisplayFunc(display_wireframe_cube)
    glutReshapeFunc(reshape)  # Added reshape function
    init()

    # Run the OpenGL loop
    glutMainLoop()

    # Capture the OpenGL rendering to an OpenCV image
    width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    opengl_image = capture_opengl_to_opencv(width, height)

    # Display the captured image using OpenCV
    cv2.imshow("OpenGL Rendering - Wireframe Cube", opengl_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main_wireframe_cube()
