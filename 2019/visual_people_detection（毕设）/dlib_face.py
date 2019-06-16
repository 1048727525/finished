import dlib
import cv2 as cv
#cnn_face_detector = dlib.cnn_face_detection_model_v1("./models/dlib/mmod_human_face_detector.dat")
cnn_face_detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("./models/dlib/shape_predictor_5_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("./models/dlib/dlib_face_recognition_resnet_model_v1.dat")
win = dlib.image_window()
img = dlib.load_rgb_image("11.png")
win.clear_overlay()
win.set_image(img)
dets = cnn_face_detector(img, 1)
for k, d in enumerate(dets):
    shape = sp(img, d)
    win.clear_overlay()
    win.add_overlay(d)
    win.add_overlay(shape)
    face_descriptor = facerec.compute_face_descriptor(img, shape)
    print(face_descriptor)
    '''''
    face_chip = dlib.get_face_chip(img, shape)
    face_descriptor_from_prealigned_image = facerec.compute_face_descriptor(face_chip)
    print(face_descriptor_from_prealigned_image)
    '''''
    dlib.hit_enter_to_continue()