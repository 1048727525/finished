import math
import csv
import numpy as np
res = 'kind'
treeList = []
class TreeNode:
    def __init__(self):
        self.child = []
        self.key = None
        self.value = None
        self.label = 0# 0是节点，1是叶节点
        self.res = -1#-1为节点，0为坏瓜，1为好瓜
        self.dict = {}
        self.isgrowed = 0
        self.tag = -1


    def growTree(self):

        if self.isgrowed == 1:
            return 1
        else:
            self.isgrowed = 1
        entropy = computeEntropy(self.dict[res])
        InfGainList = []
        keyList = []
        for key in self.dict.keys():
            InfGainList.append(computeInfGain(entropy, self.dict[key], self.dict[res]))
            keyList.append(key)
        InfGainList.pop()
        #print(self.dict.keys())
        #print(InfGainList)
        next_node_dict_list = []
        next_node_value = []
        save_node_key = []
        best_key = keyList[np.argmax(InfGainList)]
        self.key = best_key
        if np.max(InfGainList) == 0:
            self.label = 1
            self.res = self.dict[res][0]
            return 1
        for key in self.dict.keys():
            if key != best_key:
                save_node_key.append(key)
        #print(self.dict[best_key])
        for key_num in range(len(self.dict[best_key])):
            #print(len(self.dict[keyList[best_key]]))
            #print(self.dict[best_key][key_num])
            if self.dict[best_key][key_num] in next_node_value:
                key_index = next_node_value.index(self.dict[best_key][key_num])
                for key in save_node_key:
                    next_node_dict_list[key_index][key].append(self.dict[key][key_num])
            else:
                next_node_value.append(self.dict[best_key][key_num])
                Node_dict = {}
                for key in save_node_key:
                    Node_dict[key] = []
                    Node_dict[key].append(self.dict[key][key_num])
                next_node_dict_list.append(Node_dict)
        #print(next_node_value)
        #print(next_node_dict_list)
        new_node_num = len(next_node_value)

        for i in range(new_node_num):
            new_node = TreeNode()
            new_node.value = next_node_value[i]
            new_node.dict = next_node_dict_list[i]
            new_node.tag = len(treeList)
            self.child.append(new_node.tag)
            treeList.append(new_node)




def computeEntropy(inputList):
    dict = {}
    for key in inputList:
        dict[key]=dict.get(key,0) + 1
    entropy = 0.0
    values = dict.values()
    valuesSum = sum(values)
    for value in values:
        p = value/valuesSum
        entropy += -p*math.log(p,2)
    return entropy

def computeInfGain(entropy, inputList, resList):
    InfGain = computeEntropy(resList)
    dict = {}
    listLen = len(inputList)
    for key in range(listLen):
        if(dict.get(inputList[key], 0)==0):
            list = [resList[key]]
            dict[inputList[key]] = list
        else:
            dict[inputList[key]].append(resList[key])
    #print(dict)
    for key,value in dict.items():
        a = len(value)/listLen*computeEntropy(value)
        InfGain += -len(value)/listLen*computeEntropy(value)
    return InfGain



mat = []
dict = {}
with open("mellen_train.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        mat.append(line)
sum_row = len(mat)
sum_col = len(mat[0])
#print(mat)

for m in range(sum_col):
    col = []
    for i in range(sum_row):
        col.append(mat[i][m])
    dict[col[0]] = col[1:]
#print(dict)
root = TreeNode()
root.dict = dict
root.tag = 0
treeList.append(root)
root.growTree()
for node in treeList:
    node.growTree()

test_dict = dict
test_dict.pop(res)
print(test_dict)
test_dict['res'] = []
test_key = []
res = []
for key in test_dict.keys():
    test_key.append(key)
test_num = len(test_dict[test_key[0]])
for num in range(test_num):
    start_tag = 0
    start_key = treeList[start_tag].key
    next_key = None
    stop_label = 0

    while True:
        if next_key != None:
            start_key = next_key
        for child in treeList[start_tag].child:
            if treeList[child].value == test_dict[start_key][num]:
                next_key = treeList[child].key
                start_tag = child
                print(next_key)
                if treeList[child].res != -1:
                    res.append(treeList[child].res)
                    stop_label = 1
                break
        if stop_label == 1:
            break
print(res)
'''
for x in treeList:
    print("tag="+str(x.tag))
    print("key="+str(x.key))
    print("value="+str(x.value))
    print("dict="+str(x.dict))
    print("res="+str(x.res))
    print("child="+str(x.child))
    print("\n")
print(len(treeList))
'''