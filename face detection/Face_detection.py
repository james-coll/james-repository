import cv2 #pip install opencv-python

# Load the cascade
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
# use android cam ("https://0.0.0.0:0000/mjpegfeed?640x480")

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect body parts
    eye = eye_cascade.detectMultiScale(gray, 1.1, 4)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each body part
    for (x, y, w, h) in eye:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()
