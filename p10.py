# library
import cv2

# open the image
img = cv2.imread('download.jpeg')

# face cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# face detection function
def detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=3)
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,0,255), 2)
        
    return face_img

# apply the face detection function
face_img = detect_face(img)

# display the result
cv2.imshow('Original Image', img)
cv2.imshow('Detected Face', face_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# face detection:


# # library
# import cv2

# # face cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # face detection function
# def detect_face(img):
    
#     face_img = img.copy()
    
#     face_rects = face_cascade.detectMultiScale(face_img, scaleFactor=1.3, minNeighbors=3)
    
#     for (x,y,w,h) in face_rects:
#         roi = face_img[y:y+h,x:x+w]
#         blurred = cv2.medianBlur(roi,15)
#         face_img[y:y+h,x:x+w] = blurred        
#         cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,0,255), 2)
        
#     return face_img

# # open the webcam
# cap = cv2.VideoCapture(0)

# # apply the face detection
# while True:
#     ret, frame = cap.read(0)
#     frame = detect_face(frame)
#     cv2.imshow('Webcam Face Detect', frame)
#     k = cv2.waitKey(1)
#     if k == 27:
#         break
        
# cap.release()
# cv2.destroyAllWindows()