import dlib
import cv2 as cv
import time
#fd = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1("./models/dlib/mmod_human_face_detector.dat")
predictor = dlib.shape_predictor('./models/dlib/shape_predictor_68_face_landmarks.dat')
cap = cv.VideoCapture(0)
win = dlib.image_window()
while True:
    ret, frame = cap.read()
    start = time.time()
    detected_faces = cnn_face_detector(frame, 1)
    print(time.time() - start)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    win.set_image(frame)
    #:convert dlib.mmod_rectangle to dlib.rectangle
    #:refer http://dlib.net/cnn_face_detector.py.html
    rects = dlib.rectangles()
    rects.extend([d.rect for d in detected_faces])
    win.clear_overlay()
    win.add_overlay(rects)
    for i, x in enumerate(rects):
        landmarks = predictor(frame, x)
        win.add_overlay(landmarks)
