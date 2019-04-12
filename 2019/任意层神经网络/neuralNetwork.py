import numpy as np
import scipy.special
import time


class neuralNetwork:

    def __init__(self, inputnodes = 3, hiddennodes = 3, outputnodes = 3, learningrate = 0.3):
        self.nodes = [inputnodes]
        if type(hiddennodes) == int:
            self.nodes.append(hiddennodes)
        else:
            self.nodes = self.nodes + hiddennodes
        self.nodes.append(outputnodes)
        self.len_hiddennode = len(self.nodes) - 2
        self.para = []
        for i in range(self.len_hiddennode + 1):
            x = np.random.normal(0.0, pow(self.nodes[i + 1], -0.5), (self.nodes[i + 1], self.nodes[i]))
            self.para.append(x)
        self.activation_function = lambda x: scipy.special.expit(x)
        self.hiddenNodes_inputs = []
        self.hiddenNodes_outputs = []
        self.lr = learningrate

    def train(self, inputs_list, targets_list):
        inputs = np.array(inputs_list, ndmin=2).T
        targets = np.array(targets_list, ndmin=2).T
        final_outputs = self.query(inputs_list)
        output_errors = targets - final_outputs
        hidden_errors = []
        for i in range(self.len_hiddennode + 1):
            label = -1-i
            if label == -1:
                self.para[label] += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                             np.transpose(self.hiddenNodes_outputs[label]))
                hidden_errors = np.dot(self.para[-1].T, output_errors)
            elif label == -1 - self.len_hiddennode:
                self.para[label] += self.lr * np.dot((hidden_errors * self.hiddenNodes_outputs[label+1] * (1.0 - self.hiddenNodes_outputs[label+1])),
                                                     np.transpose(inputs))
            else:
                self.para[label] += self.lr * np.dot((hidden_errors * self.hiddenNodes_outputs[label+1] * (1.0 - self.hiddenNodes_outputs[label+1])),
                                                     np.transpose(self.hiddenNodes_outputs[label]))
                hidden_errors = np.dot(self.para[label].T, hidden_errors)
        pass

    #forward the net
    def query(self, inputs_list):
        inputs = np.array(inputs_list, ndmin=2).T
        self.hiddenNodes_inputs = []
        self.hiddenNodes_outputs = []
        for i in range(self.len_hiddennode):
            if i == 0:
                x = np.dot(self.para[0], inputs)
            else:
                x = np.dot(self.para[i], self.hiddenNodes_outputs[i - 1])
            self.hiddenNodes_inputs.append(x)
            self.hiddenNodes_outputs.append(self.activation_function(x))
        final_input = np.dot(self.para[-1], self.hiddenNodes_outputs[-1])
        final_output = self.activation_function(final_input)
        return final_output


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
