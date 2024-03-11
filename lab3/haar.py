from __future__ import print_function
import cv2 as cv
import argparse
from picamera2 import Picamera2


def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    timestamp = cv.getTickCount()
    iter = 0
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255))
        faceROI = frame_gray[y:y+h,x:x+w]
        # 100x100 with interpolation
        faceROI = cv.resize(faceROI, (100, 100), interpolation=cv.INTER_LINEAR)
        # cv.imwrite(f'data/face_{timestamp}_{iter}.jpg', faceROI)
        iter += 1


    # cv.imshow('Capture - Face detection', frame)

parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
parser.add_argument('--face_cascade', help='Path to face cascade.', default='data/haarcascade_frontalface_default.xml')
parser.add_argument('--camera', help='Camera divide number.', type=int, default=0)
args = parser.parse_args()
face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()
#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)
# camera_device = args.camera
picam2 = Picamera2()
#-- 2. Read the video stream
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()
# cap = cv.VideoCapture(camera_device)
# if not cap.isOpened:
#     print('--(!)Error opening video capture')
#     exit(0)
while True:
    frame = picam2.capture_array()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break