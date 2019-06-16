import dlib
import openface
import numpy as np
import sys
import os
import pickle
import time
import cv2 as cv
from widget import Ui_Widget  # 这里的first是.ui文件生成的.py文件名
from PyQt5.QtWidgets import QFileDialog, QApplication, QWidget, QMessageBox, QGraphicsView, QCheckBox, QGridLayout
from PyQt5.QtGui import QPixmap, QImage, QPainter, QFont, QPen, QColor
from PyQt5.QtCore import QThread, Qt, pyqtSignal, QTimer, QTime, QDate, QMutex
from shutil import copyfile
import shutil
main_dir = "/home/wz/"
real_dir = main_dir + "PycharmProjects/visual_people_detection/"
np.set_printoptions(precision=2)
class myThread(QThread):

    cnn_face_detector = dlib.cnn_face_detection_model_v1("./models/dlib/mmod_human_face_detector.dat")
    changePixmap = pyqtSignal(QImage)
    get_rejected_face = pyqtSignal(QImage)
    get_detected_face = pyqtSignal(QImage)
    INTERVAL = 10
    align = openface.AlignDlib("./models/dlib/shape_predictor_68_face_landmarks.dat")
    net = openface.TorchNeuralNet("./models/openface/nn4.small2.v1.t7", imgDim=96,
                                  cuda=True)
    pause = QMutex()
    confidence = 0.8
    selected_people = []
    save_show_label = (0, 0)
    store_label = 0
    video_path = "./video/intern/1.mp4"
    #video_path = "./video/oldfriend/4.mkv"
    #video_path = "2.mp4"
    save_main_num = 0

    with open("./generated-embeddings/classifier.pkl", 'rb') as f:
        if sys.version_info[0] < 3:
            (le, clf) = pickle.load(f)
        else:
            (le, clf) = pickle.load(f, encoding='latin1')

    def align_picture(self, rect, rbgimg):
        print("size is {}".format(rbgimg.shape))
        alignedFace = self.align.align(
            96,
            rbgimg,
            rect,
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        return alignedFace#:type(aligenedFace) = <class 'numpy.ndarray'>

    def get_prediction(self, rect, rbgimg):
        start = time.time()
        alignedFace = self.align_picture(rect, rbgimg)
        rep = self.net.forward(alignedFace)
        print("Neural network forward pass took {} seconds.".format(
                time.time() - start))
        rep = rep.reshape(1, -1)
        start = time.time()
        predictions = self.clf.predict_proba(rep).ravel()
        maxI = np.argmax(predictions)
        person = self.le.inverse_transform(maxI)
        confidence = predictions[maxI]
        print("Prediction took {} seconds.".format(time.time() - start))
        return person, confidence

    def get_faces(self, rgbImage):
        start_time = time.time()
        detected_faces = self.cnn_face_detector(rgbImage, 1)
        rects = dlib.rectangles()
        rects.extend([d.rect for d in detected_faces])
        print("Face detection spend {}s".format(time.time() - start_time))
        return rects#:type = <class 'dlib.rectangles'>

    def run(self):
        #cap = cv.VideoCapture(0)
        cap = cv.VideoCapture(self.video_path)
        frame_timer1 = 0
        box_color = (255, 0, 0)
        myQPen = QPen()
        myQFont = QFont()
        myQFont.setPixelSize(20)
        print(self.save_show_label[0])
        if self.save_show_label[0] != 0:
            fps = cap.get(cv.CAP_PROP_FPS)
            size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)),
                    int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
            vw = cv.VideoWriter("./result/" + "test.mp4", cv.VideoWriter_fourcc(*'mp4v'), fps, size)
        while (cap.isOpened()==True):
            self.pause.lock()
            ret, frame = cap.read()
            if ret:
                rgbImage = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                Qface = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0],
                                        QImage.Format_RGB888)
                #:proess the image
                if frame_timer1 % self.INTERVAL == 0:
                    rects = self.get_faces(rgbImage)
                    color_list = []
                    person_name_list = []
                    for rect in rects:
                        person, confidence = self.get_prediction(rect, rgbImage)
                        person_name = "unknown"
                        if ((person.decode() in self.selected_people) == True) and confidence>self.confidence:
                            self.store_label = 1
                            person_name = person.decode()
                            box_color = (255, 0, 0)
                            color_list.append(box_color)
                            person_name_list.append(person_name)
                            Qdetected_face = Qface.copy(rect.left(), rect.top(), rect.width(), rect.height())
                            #:在匹配的人脸上写字
                            if self.save_show_label[1] == 1:
                                myQPainter = QPainter(Qdetected_face)
                                myQFont.setPixelSize(int(rect.width()/5))
                                myQPen.setColor(Qt.red)
                                myQPainter.setPen(myQPen)
                                myQPainter.setFont(myQFont)
                                myQPainter.drawText(Qdetected_face.rect(), Qt.AlignTop, str(round(confidence, 3)))
                                myQPainter.end()
                                #发送信号
                                self.get_detected_face.emit(Qdetected_face)
                            #在视屏中框出人脸
                            cv.rectangle(rgbImage, (rect.left(), rect.top()), (rect.right(), rect.bottom()), box_color, 2)
                            cv.putText(rgbImage, person_name, (rect.left(), rect.top()), cv.FONT_HERSHEY_PLAIN, rect.width()/80, box_color,2)

                        else:
                            self.store_label = 0
                            person_name = "unknown"
                            Qrejected_face = Qface.copy(rect.left(), rect.top(), rect.width(), rect.height())
                            box_color = (0, 255, 0)
                            color_list.append(box_color)
                            person_name_list.append(person_name)
                            #:在匹配的人脸上写字
                            myQPainter = QPainter(Qrejected_face)
                            myQFont.setPixelSize(int(rect.width() / 5))
                            myQPen.setColor(Qt.green)
                            myQPainter.setPen(myQPen)
                            myQPainter.setFont(myQFont)
                            myQPainter.drawText(Qrejected_face.rect(), Qt.AlignTop, str(round(confidence, 3)))
                            myQPainter.end()
                            # 发送信号
                            self.get_rejected_face.emit(Qrejected_face)
                            # 在视屏中框出人脸
                            cv.rectangle(rgbImage, (rect.left(), rect.top()), (rect.right(), rect.bottom()), box_color, 2)
                            cv.putText(rgbImage, person_name, (rect.left(), rect.top()), cv.FONT_HERSHEY_PLAIN, rect.width()/80, box_color, 2)
                    if self.save_show_label[0] != 0:
                        vw.write(cv.cvtColor(rgbImage, cv.COLOR_BGR2RGB))
                    #:for test###
                    QrgbImage = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                    QrgbImage.save("./saved_image/main/{}.jpg".format(self.save_main_num), "JPG", 100)
                    self.save_main_num = self.save_main_num + 1
                    #############

                else:
                    for i, rect in enumerate(rects):
                        cv.rectangle(rgbImage, (rect.left(), rect.top()), (rect.right(), rect.bottom()), color_list[i], 2)
                        cv.putText(rgbImage, person_name_list[i], (rect.left(), rect.top()), cv.FONT_HERSHEY_PLAIN, rect.width()/80, color_list[i], 2)
                        pass
                    if self.save_show_label[0] == 2:
                        vw.write(cv.cvtColor(rgbImage, cv.COLOR_BGR2RGB))
                    elif self.save_show_label[0] == 1:
                        if self.store_label == 1:
                            vw.write(cv.cvtColor(rgbImage, cv.COLOR_BGR2RGB))
                if self.save_show_label[1] == 1:
                    QrgbImage = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
                    self.changePixmap.emit(QrgbImage)
                frame_timer1 = (frame_timer1 + 1)%self.INTERVAL
                #time.sleep(0.01) #控制视频播放的速度
            else:
                break
            self.pause.unlock()




# 这个类继承界面UI类
class mywindow(QWidget, Ui_Widget):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.window().setWindowTitle("人物检索系统")
        self.pic_list = [self.map1, self.map2, self.map3, self.map4, self.map5, self.map6, self.map7,
                    self.map8, self.map9, self.map10]
        self.detected_face = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8]
        self.rejected_face = [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.r8]
        self.trained_people_list = []
        if os.path.exists("./training-images"):
            self.trained_people_list = os.listdir("./training-images")
        if os.path.exists("./saved_image/accept"):
            shutil.rmtree("./saved_image/accept")
        if os.path.exists("./saved_image/main"):
            shutil.rmtree("./saved_image/main")
        if os.path.exists("./saved_image/reject"):
            shutil.rmtree("./saved_image/reject")
        os.mkdir("./saved_image/accept")
        os.mkdir("./saved_image/main")
        os.mkdir("./saved_image/reject")

        self.pushButton.clicked.connect(self.FindDir)
        self.pushButton_2.clicked.connect(self.ClearPic)
        self.listWidget.itemDoubleClicked.connect(self.RemovePic)
        self.pushButton_3.clicked.connect(self.Submit)
        self.pushButton_4.clicked.connect(self.Reset)
        self.pushButton_5.clicked.connect(self.Train)
        self.pushButton_6.clicked.connect(self.click_btn_start)
        self.btn_pause.clicked.connect(self.click_btn_pause)
        self.detected_face_list_num = 0
        self.detected_face_list_len = len(self.detected_face)
        self.rejected_face_list_num = 0
        self.rejected_face_list_len = len(self.rejected_face)
        #lcd时间显示
        self.lcdNumber.setDigitCount(8)
        self.ShowColn = True
        self.timer1 = QTimer(self)
        self.timer1.start(1000)
        self.timer1.timeout.connect(self.showTime)
        now_data = QDate.currentDate()
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.display(now_data.toString(Qt.ISODate))
        self.th = myThread()
        self.lock_or_not = False
        self.spinBox.setValue(20)
        self.doubleSpinBox.setValue(0.60)
        self.doubleSpinBox.setSingleStep(0.01)
        #人物复选框
        self.vLayout = QGridLayout()
        self.check_box_list = []
        for file in os.listdir("./training-images"):
            self.check_box_name = QCheckBox(file, self)
            self.vLayout.addWidget(self.check_box_name)
            self.check_box_list.append(self.check_box_name)
        self.scrollArea.widget().setLayout(self.vLayout)
        self.selected_people = []
        self.comboBox.addItem("not save")
        self.comboBox.addItem("save key sections")
        self.comboBox.addItem("save total sections")
        self.save_or_not = (0, 0)
        self.save_num_a = 0
        self.save_num_r = 0
        self.save_num_m = 0

    def click_btn_pause(self):
        print(self.th.isRunning())
        if self.lock_or_not == False:
            self.th.pause.lock()
            self.lock_or_not = True
        else:
            self.th.pause.unlock()
            self.lock_or_not = False

    def showTime(self):
        time = QTime.currentTime()
        time_text = time.toString(Qt.ISODate)
        if self.ShowColn == True:
            self.ShowColn = False
        else:
            time_text = time_text.replace(':', ' ')
            self.ShowColn = True
        self.lcdNumber.display(time_text)

    def FindDir(self):
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取图像", "/home", "picture Files (*.png *.jpg)")
        self.listWidget.addItem(fileName)
        self.update_Train_classier()

    def RemovePic(self, item):
        self.listWidget.removeItemWidget(item)
        self.listWidget.takeItem(self.listWidget.row(item))
        self.update_Train_classier()

    def ClearPic(self):
        self.listWidget.clear()
        self.update_Train_classier()

    def update_Train_classier(self):
        for i in range(len(self.pic_list)):
            self.pic_list[i].clear()
        for i in range(self.listWidget.count()):
            self.pic_list[i%10].setScaledContents(True)
            self.pic_list[i%10].setPixmap(QPixmap(self.listWidget.item(i).text()))

    def Submit(self):
        people_name = self.lineEdit.text()
        print(people_name)
        if (people_name in self.trained_people_list) == False:
            os.mkdir("./training-images/" + people_name)
        for i in range(self.listWidget.count()):
            #:submit the pictures we choiced to the directory named "training-images"
            choiced_name = self.listWidget.item(i).text()
            dst = "./training-images/" + people_name + "/" + choiced_name.split('/')[-1]
            copyfile(choiced_name, dst)
        self.Reset()

    def Reset(self):
        self.label_2.clear()
        self.ClearPic()
        self.lineEdit.clear()

    def Train(self):
        if os.path.exists(main_dir + "openface") == False:
            QMessageBox.critical(self, "错误", "Please ensure openface has been installed!")
        else:
            self.label_2.setText("Waititing...")
            QApplication.processEvents()
            startTime = time.time()
            os.system("rm -rf ./aligned-images/")
            os.system("python2 {}openface/util/align-dlib.py ./training-images/ align outerEyesAndNose ./aligned-images/ --size 96;".format(main_dir))
            os.system("{}openface/batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/".format(main_dir))
            print("{}openface/batch-represent/main.lua -outDir ./generated-embeddings/ -data ./aligned-images/".format(main_dir))
            os.system("python2 ./checkout.py train ./generated-embeddings/")
            self.label_2.setText("Training has been finished, cost {}s".format(time.time() - startTime))

    def click_btn_start(self):
        if self.lock_or_not == True:
            self.th.pause.unlock()
            self.lock_or_not = False
        #记录复选框的内容
        self.selected_people = []
        for i in self.check_box_list:
            if i.isChecked() == True:
                self.selected_people.append(i.text())
        self.th.confidence = 0.8
        self.th.selected_people = self.selected_people
        self.th.INTERVAL = self.spinBox.value()
        self.th.confidence = self.doubleSpinBox.value()
        if self.comboBox.currentText() == "not save":
            self.th.save_show_label = (0, 1)
        elif self.comboBox.currentText() == "save key sections":
            self.th.save_show_label = (1, 1)
        else:
            self.th.save_show_label = (2, 1)
        self.th.changePixmap.connect(self.setImage)
        self.th.get_detected_face.connect(self.show_detected_face)
        self.th.get_rejected_face.connect(self.show_rejected_face)
        self.th.start()

    def setImage(self, image):
        image = image.scaled(self.frame_2.width(), self.frame_2.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #image.save("./saved_image/main/{}.jpg".format(self.save_num_m), "JPG", 100)
        #self.save_num_m += 1
        self.label_3.setPixmap(QPixmap.fromImage(image))

    def show_rejected_face(self, image):
        image = image.scaled(self.r1.width(), self.r1.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        #self.r1.setPixmap(QPixmap.fromImage(image))
        image.save("./saved_image/reject/{}.jpg".format(self.save_num_r), "JPG", 100)
        self.save_num_r += 1
        self.rejected_face[self.rejected_face_list_num % self.rejected_face_list_len].setPixmap(QPixmap.fromImage(image))
        self.rejected_face_list_num = (self.rejected_face_list_num + 1) % self.rejected_face_list_len

    def show_detected_face(self, image):
        image = image.scaled(self.d1.width(), self.d1.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        image.save("./saved_image/accept/{}.jpg".format(self.save_num_a), "JPG", 100)
        self.save_num_a += 1
        self.detected_face[self.detected_face_list_num % self.detected_face_list_len].setPixmap(QPixmap.fromImage(image))
        self.detected_face_list_num = (self.detected_face_list_num + 1) % self.detected_face_list_len

#调用show
if __name__=="__main__":
    app=QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

