import cv2 as cv
import numpy as np
img = (500,500)
blank = np.zeros(img, dtype = 'uint8')


cv.rectangle(blank,(150,0), (300,280), (200,0,0), thickness=-1)
cv.rectangle(blank,(0,0), (150,280), (100,0,0), -1)


cv.circle(blank, (300,280), 40, (255,255,255), -1)

cv.imshow('blank', blank)
cv.waitKey(0)

cv.destroyAllWindows()