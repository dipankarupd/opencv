import cv2
import numpy as np
import math

def rotate_3d_cube(img, angle):
    # Cube vertices
    vertices = np.array([[-1, -1, -1],
                         [1, -1, -1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, 1],
                         [-1, 1, 1]], dtype=np.float32)

    # Rotation matrix around the X-axis
    rotation_matrix = np.array([[1,0,0],
                                [0, math.cos(angle), -math.sin(angle)],
                                [0, math.sin(angle), math.cos(angle)]], dtype=np.float32)

    # Rotate the cube vertices in 3D space
    rotated_vertices = np.dot(vertices, rotation_matrix)

    # Project the 3D points to 2D
    projected_vertices = (rotated_vertices[:, :2] * 100 + np.array([200, 200])).astype(int)

    # Define cube edges
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    # Draw cube edges
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(img, pt1, pt2, (0, 255, 0), 2)

    return img

def main():
    angle = 0

    while True:
        frame = np.zeros((400, 400, 3), dtype=np.uint8)

        # Rotate and draw the 3D cube
        frame = rotate_3d_cube(frame, angle)

        cv2.imshow("Rotating 3D Cube", frame)

        # Update angle for rotating the 3D cube
        angle += 0.02

        key = cv2.waitKey(30)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
