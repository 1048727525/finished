import numpy as np
import scipy.special
import time


class neuralNetwork:

    def __init__(self, inputnodes = 3, hiddennodes = 3, outputnodes = 3, learningrate = 0.3):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        #简单的权重初始方法
        #self.wih = np.random.rand(self.hnodes, self.inodes) - 0.5
        #self.who = np.random.rand(self.onodes, self.hnodes) - 0.5
        #较为复杂的权重初始方法，但更加有效
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
        pass

    #forward the net
    def query(self, inputs_list):
        #convert inputs list to 2d array
        inputs = np.array(inputs_list, ndmin=2).T
        #calculate the signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_input = np.dot(self.who, hidden_outputs)
        final_output = self.activation_function(final_input)
        return final_output
        pass


if __name__ == '__main__':
    start = time.time()
    input_nodes = 784
    hidden_nodes = 100
    output_nodes = 10
    learning_rate = 0.3
    data_file = open("mnist_train.csv", 'r')
    data_list = data_file.readlines()
    data_file.close()
    net = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
    for record in data_list:
        all_values = record.split(',')
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        targets = np.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        net.train(inputs, targets)
    train_end = time.time()
    print("train spent", (train_end - start), "s")
    test_data_file = open("mnist_test.csv", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
    correct = 0
    for record in test_data_list:
        all_values = record.split(',')
        correct_label = int(all_values[0])
        #print(correct_label, "correct label")
        inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = net.query(inputs)
        label = np.argmax(outputs)
        #print(label, "network's answer")
        if(label == correct_label):
            correct += 1
    sum = len(test_data_list)
    test_end = time.time()
    print("test spent ", (test_end - train_end), "s")
    print("correct rate is ", float(correct/sum))