import cv2 as cv
import numpy as np


def calculateCentroid(vertices):
    return int((vertices[0][0] + vertices[1][0] + vertices[2][0])/3) , int((vertices[0][1] + vertices[1][1] + vertices[2][1]))/31

blank = np.zeros((500,500, 3), np.uint8)

vertices = np.array([[250,100],[100,400],[400,400]], np.int32)

init_color = (0,255,0)

while True:
    img = blank.copy()
    
    cv.fillPoly(img, [vertices.reshape((-1,1,2))], color=init_color)
    
    centroid = calculateCentroid(vertices)
    
    cv.circle(img, centroid, 5, (255,255,255), -1)
    
    cv.imshow('output', img)
    
    key = cv.waitKey(0) & 0xff
    
    if key == ord('r'):
        init_color = (255,0,0)
    
    elif key == ord('b'):
        init_color = (0,0,255)
        
        
    elif key == 27:  # Esc key
        break

# Close all open windows
cv.destroyAllWindows()