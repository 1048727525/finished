#!/usr/bin/env python2
#coding:utf-8
import csv
import time
import dlib
start = time.time()
import argparse
import cv2
import cv2 as cv
import os
import pickle
import sys
from operator import itemgetter
import numpy as np
np.set_printoptions(precision=2)
import pandas as pd
import openface
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.mixture import GMM
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

fileDir = "/home/wz/openface"
modelDir = fileDir + "/models"
#modelDir = os.path.join(fileDir, '..', 'models')
dlibModelDir = modelDir + "/dlib"
openfaceModelDir = modelDir + "/openface"

class find_face:
    def __init__(self):
        self.fd = dlib.cnn_face_detection_model_v1(dlibModelDir + "/mmod_human_face_detector.dat")
    def getAllFaceBoundingBoxes_cun(self, img):
        detected_faces = self.fd(img, 1)
        res = []
        for i, x in enumerate(detected_faces):
            #if type(x) == dlib.mmod_rectangles:
                #detected_faces[i] = dlib.rectangle(x.rect.left(), x.rect.top(), x.rect.right(), x.rect.bottom())
            res.append(dlib.rectangle(x.rect.left(), x.rect.top(), x.rect.right(), x.rect.bottom()))
        return res

    def getLargestFaceBoundingBox(self, img, skipMulti=False):
        faces = self.getAllFaceBoundingBoxes(img)
        if (not skipMulti and len(faces) > 0) or len(faces) == 1:
            return max(faces, key=lambda rect: rect.width() * rect.height())
        else:
            return None

def getRep(img, multiple=False):
    start = time.time()
    bgrImg = img
    if bgrImg is None:
        raise Exception("Unable to load image: {}".format(imgPath))

    rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

    if args.verbose:
        print("  + Original size: {}".format(rgbImg.shape))
    if args.verbose:
        print("Loading the image took {} seconds.".format(time.time() - start))

    start = time.time()

    if multiple:
        #Returns:	All face bounding boxes in an image.
        #Return type:	dlib.rectangles
        #bbs = align.getAllFaceBoundingBoxes(rgbImg)
        bbs = find_face_cnn.getAllFaceBoundingBoxes_cun(rgbImg)
    else:
        bb1 = find_face_cnn.getLargestFaceBoundingBox(rgbImg)
        bbs = [bb1]
    if len(bbs) == 0 or (not multiple and bb1 is None):
        print("Unable to find a face")

    if args.verbose:
        print("Face detection took {} seconds.".format(time.time() - start))

    reps = []
    for bb in bbs:
        start = time.time()
        #Return type:numpy.ndarray
        #Returns:	The aligned RGB image. Shape: (imgDim, imgDim, 3)
        #The alignment preprocess faces for input into a neural network.
        # Faces are resized to the same size (such as 96x96)
        #and transformed to make landmarks (such as the eyes and nose) appear at the same location on every image.
        alignedFace = align.align(
            args.imgDim,
            rgbImg,
            bb, #type = dlib.rectangle
            landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        if alignedFace is None:
            raise Exception("Unable to align image: {}".format(imgPath))
        if args.verbose:
            print("Alignment took {} seconds.".format(time.time() - start))
            print("This bbox is centered at {}, {}".format(bb.center().x, bb.center().y))
        start = time.time()
        #网络的前向传播 Return type:numpy.ndarray
        #返回其网络生成的128个特征值的权重
        rep = net.forward(alignedFace)
        if args.verbose:
            print("Neural network forward pass took {} seconds.".format(
                time.time() - start))
        reps.append((bb.center().x, rep))
        #按照从左至右的顺序将人脸参数依次排序
    sreps = sorted(reps, key=lambda x: x[0])
    return sreps

def train(args):
    print("Loading embeddings.")
    fname = "{}/labels.csv".format(args.workDir)
    labels = pd.read_csv(fname, header=None).as_matrix()[:, 1]
    labels = map(itemgetter(1),
                 map(os.path.split,
                     map(os.path.dirname, labels)))  # Get the directory.
    fname = "{}/reps.csv".format(args.workDir)
    embeddings = pd.read_csv(fname, header=None).as_matrix()
    le = LabelEncoder().fit(labels)
    labelsNum = le.transform(labels)
    nClasses = len(le.classes_)
    print("Training for {} classes.".format(nClasses))

    if args.classifier == 'LinearSvm':
        clf = SVC(C=1, kernel='linear', probability=True)
    elif args.classifier == 'GridSearchSvm':
        print("""
        Warning: In our experiences, using a grid search over SVM hyper-parameters only
        gives marginally better performance than a linear SVM with C=1 and
        is not worth the extra computations of performing a grid search.
        """)
        param_grid = [
            {'C': [1, 10, 100, 1000],
             'kernel': ['linear']},
            {'C': [1, 10, 100, 1000],
             'gamma': [0.001, 0.0001],
             'kernel': ['rbf']}
        ]
        clf = GridSearchCV(SVC(C=1, probability=True), param_grid, cv=5)
    elif args.classifier == 'GMM':  # Doesn't work best
        clf = GMM(n_components=nClasses)

    # ref:
    # http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#example-classification-plot-classifier-comparison-py
    elif args.classifier == 'RadialSvm':  # Radial Basis Function kernel
        # works better with C = 1 and gamma = 2
        clf = SVC(C=1, kernel='rbf', probability=True, gamma=2)
    elif args.classifier == 'DecisionTree':  # Doesn't work best
        clf = DecisionTreeClassifier(max_depth=20)
    elif args.classifier == 'GaussianNB':
        clf = GaussianNB()

    # ref: https://jessesw.com/Deep-Learning/
    elif args.classifier == 'DBN':
        from nolearn.dbn import DBN
        clf = DBN([embeddings.shape[1], 500, labelsNum[-1:][0] + 1],  # i/p nodes, hidden nodes, o/p nodes
                  learn_rates=0.3,
                  # Smaller steps mean a possibly more accurate result, but the
                  # training will take longer
                  learn_rate_decays=0.9,
                  # a factor the initial learning rate will be multiplied by
                  # after each iteration of the training
                  epochs=300,  # no of iternation
                  # dropouts = 0.25, # Express the percentage of nodes that
                  # will be randomly dropped as a decimal.
                  verbose=1)

    if args.ldaDim > 0:
        clf_final = clf
        clf = Pipeline([('lda', LDA(n_components=args.ldaDim)),
                        ('clf', clf_final)])

    clf.fit(embeddings, labelsNum)

    fName = "{}/classifier.pkl".format(args.workDir)
    print("Saving classifier to '{}'".format(fName))
    with open(fName, 'w') as f:
        pickle.dump((le, clf), f)



def infer(args, multiple=True):
    with open(args.classifierModel, 'rb') as f:
        if sys.version_info[0] < 3:
                (le, clf) = pickle.load(f)
        else:
                (le, clf) = pickle.load(f, encoding='latin1')
        #le为将离散的label转换成0到n−1之间的数，Encode labels with value between 0 and n_classes-1.
    video1 = cv2.VideoCapture(args.video)
    #video1 = cv2.VideoCapture("/home/wz/work/video/old friend.mkv")
    #INTERVAL = 20
    INTERVAL = args.interval
    frame_counter = 0
    store_check = False
    #contiune_check = False
    #videoWriter = cv2.VideoWriter()
    fps = video1.get(cv2.CAP_PROP_FPS)
    size = (int(video1.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    realPath = os.path.dirname(os.path.realpath(__file__))
    print("store video")
    videoWriter = cv2.VideoWriter(realPath + "/result/" + sys.argv[5].split('/')[-1],
                                  cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    print(realPath + "/result/" + sys.argv[5].split('/')[-1],
                                  cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    csvFile = open(sys.argv[5].split('/')[-1]+".csv", "w")
    lablecsvFile = open("label" + sys.argv[5].split('/')[-1]+".csv", "w")
    Path1 = fileDir + "/training-images/"
    names = os.listdir(Path1)
    NamesNum = len(names)
    for x in range(NamesNum):
        names[x] = le.inverse_transform(x)
    print(names)
    writer1 = csv.writer(csvFile)
    writer2 =csv.writer(lablecsvFile)
    writer1.writerow(names)
    writer2.writerow(["frame"])
    while True:
        ret, frame = video1.read()
        if ret == False:
            break
        if frame_counter % INTERVAL == 0:
            rgbImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            reps = getRep(rgbImg, multiple)
            if len(reps) > 1:
                print("List of faces in image from left to right")
            for r in reps:
                # 对特征值的形式进行转换，将其转换成一行
                rep = r[1].reshape(1, -1)
                bbx = r[0]
                start = time.time()
                # 对 rep 进行预测，返回各个预测标签上的概率
                #labels = clf.predict(rep)
                predictions = clf.predict_proba(rep).ravel()

                maxI = np.argmax(predictions)
                x = predictions
                writer1.writerow(x)
                print(frame_counter)
                writer2.writerow([frame_counter])
                # 找出预测概率最大的那个结果的下标
                person = le.inverse_transform(maxI)

                #获取各个人脸可能的概率
                confidence = predictions[maxI]
                if args.verbose:
                    print("Prediction took {} seconds.".format(time.time() - start))
                if multiple:
                    print("Predict {} @ x={} with {:.2f} confidence.".format(person.decode('utf-8'), bbx,
                                                                             confidence))
                else:
                    print("Predict {} with {:.2f} confidence.".format(person.decode('utf-8'), confidence))
                if isinstance(clf, GMM):
                    dist = np.linalg.norm(rep - clf.means_[maxI])
                    print("  + Distance from the mean: {}".format(dist))
                #if person == "Rachel" and confidence > 0.80:
                if person == args.people and confidence > args.confidence:
                    store_check = True
                    #frame_counter = frame_counter + 1
                    videoWriter.write(frame)
                    break
                else:
                    store_check = False
        elif store_check == True:
                videoWriter.write(frame)
        frame_counter = frame_counter + 1
    video1.release()
    csvFile.close()
    lablecsvFile.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--dlibFacePredictor',
        type=str,
        help="Path to dlib's face predictor.",
        default=os.path.join(
            dlibModelDir,
            "shape_predictor_68_face_landmarks.dat"))
    parser.add_argument(
        '--networkModel',
        type=str,
        help="Path to Torch network model.",
        default=os.path.join(
            openfaceModelDir,
            'nn4.small2.v1.t7'))
    parser.add_argument('--imgDim', type=int,
                        help="Default image dimension.", default=96)
    parser.add_argument('--cuda', action='store_true')
    parser.add_argument('--verbose', action='store_true')

    subparsers = parser.add_subparsers(dest='mode', help="Mode")
    trainParser = subparsers.add_parser('train',
                                        help="Train a new classifier.")
    trainParser.add_argument('--ldaDim', type=int, default=-1)
    trainParser.add_argument(
        '--classifier',
        type=str,
        choices=[
            'LinearSvm',
            'GridSearchSvm',
            'GMM',
            'RadialSvm',
            'DecisionTree',
            'GaussianNB',
            'DBN'],
        help='The type of classifier to use.',
        default='LinearSvm')
    trainParser.add_argument(
        'workDir',
        type=str,
        help="The input work directory containing 'reps.csv' and 'labels.csv'. Obtained from aligning a directory with 'align-dlib' and getting the representations with 'batch-represent'.")

    inferParser = subparsers.add_parser(
        'infer', help='Predict who an image contains from a trained classifier.')
    inferParser.add_argument(
        'classifierModel',
        type=str,
        help='The Python pickle representing the classifier. This is NOT the Torch network model, which can be set with --networkModel.')
    #inferParser.add_argument('imgs', type=str, nargs='+',
           #                  help="Input image.")
    inferParser.add_argument('video', help="The video you want to operate", type=str)
    inferParser.add_argument('people', help="The people you want to find", type=str)
    inferParser.add_argument('confidence', help="The confidence you need", type=float, default=0.80)
    inferParser.add_argument('interval', help="The interval between flame", type=int, default=20)
    inferParser.add_argument('--multi', help="Infer multiple faces in image",
                             action="store_true")



    args = parser.parse_args()
    if args.verbose:
        print("Argument parsing and import libraries took {} seconds.".format(
            time.time() - start))

    if args.mode == 'infer' and args.classifierModel.endswith(".t7"):
        raise Exception("""
Torch network model passed as the classification model,
which should be a Python pickle (.pkl)

See the documentation for the distinction between the Torch
network and classification models:

        http://cmusatyalab.github.io/openface/demo-3-classifier/
        http://cmusatyalab.github.io/openface/training-new-models/

Use `--networkModel` to set a non-standard Torch network model.""")
    start = time.time()
    find_face_cnn = find_face()
    align = openface.AlignDlib(args.dlibFacePredictor)
    net = openface.TorchNeuralNet(args.networkModel, imgDim=args.imgDim,
                                  cuda=args.cuda)

    if args.verbose:
        print("Loading the dlib and OpenFace models took {} seconds.".format(
            time.time() - start))
        start = time.time()

    if args.mode == 'train':
        train(args)
    elif args.mode == 'infer':

        infer(args, args.multi)
