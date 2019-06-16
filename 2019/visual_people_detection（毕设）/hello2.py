import dlib
import cv2 as cv
import time
#cnn_face_detector = dlib.get_frontal_face_detector()
cnn_face_detector = dlib.cnn_face_detection_model_v1("./models/dlib/mmod_human_face_detector.dat")
predictor = dlib.shape_predictor('./models/dlib/shape_predictor_68_face_landmarks.dat')
img = cv.imread("4.jpeg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
print(img.shape)
win = dlib.image_window()
start = time.time()
detected_faces = cnn_face_detector(img, 1)
start = time.time()
detected_faces = cnn_face_detector(img, 1)
print(time.time() - start)
rects = dlib.rectangles()
rects.extend([d.rect for d in detected_faces])
win.set_image(img)
win.add_overlay(rects)
for i, x in enumerate(rects):
    landmarks = predictor(img, x)
    win.add_overlay(landmarks)
pass