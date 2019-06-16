import cv2 as cv
import dlib
cap = cv.VideoCapture("2.mp4")
fps = cap.get(cv.CAP_PROP_FPS)
size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
vw = cv.VideoWriter("./result/" + "test.mp4", cv.VideoWriter_fourcc(*'mp4v'), fps, size)
while True:
    ret, frame = cap.read()
    print(ret)
    if ret:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        vw.write(frame)
    else:
        break