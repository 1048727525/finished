import myFuction
import classifier
import numpy as np

if __name__ == '__main__':
    trainArray1 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_1")[b'data']
    trainArray2 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_2")[b'data']
    trainArray3 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_3")[b'data']
    trainArray4 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_4")[b'data']
    trainArray5 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_5")[b'data']
    trainArray = np.vstack((trainArray1, trainArray2, trainArray3, trainArray4, trainArray5))
    label1 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_1")[b'labels']
    label2 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_2")[b'labels']
    label3 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_3")[b'labels']
    label4 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_4")[b'labels']
    label5 = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\data_batch_5")[b'labels']
    label = label1 + label2 + label3 + label4 + label5
    testArray = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\test_batch")[b'data']
    testLabel = myFuction.unpickle(".\\cifar-10-python\\cifar-10-batches-py\\test_batch")[b'labels']
    nn = classifier.KNearestNeighbor()
    nn.train(trainArray, label)
    predict = nn.predict(testArray)
    print('accuracy: %f' % (np.mean(predict == testLabel)))
    print(predict)