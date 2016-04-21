import csv
import random
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

THRESHOLD_ALCOHOL = 3.0
TESTING_SET_LIMIT = 200

def get_inputs():
    file = open('student-mat.csv', 'rb')
    file_1 = list(csv.reader(file))

    file = open('student-por.csv', 'rb')
    file_2 = list(csv.reader(file))

    del file_1[0]
    del file_2[0]
    return file_1 + file_2


def divide_dataset(features, labels):
    i = 0
    test_features = []
    test_labels = []
    while i <= TESTING_SET_LIMIT:
        index = random.randint(0, len(features)-1)
        test_features.append(features[index])
        test_labels.append(labels[index])
        del features[index]
        del labels[index]
        i += 1
    return features, labels, test_features, test_labels

def get_label_for_alcohol_comsumption(a, b):
    val = float(a*5 + b*2)
    val = val/7.0
    if val > THRESHOLD_ALCOHOL:
        return 1
    return 0


def process(input, dict, dict_start, index):
    if (dict[index].has_key(input)):
        return dict[index][input]
    dict[index][input] = dict_start[index]
    dict_start[index] += 1.0
    return dict[index][input]

def normalize_feature(result, index):
    min_value = 100000000.0
    max_value = -100000000.0
    for row in result:
        val = float(row[index])
        if val < min_value:
            min_value = val
        if val > max_value:
            max_value = val

    i = 0
    while i < len(result):
        result[i][index] = (float(result[i][index])-min_value)/(max_value-min_value)
        i += 1

def process_input_files(inputs):
    result = []
    for i in range(0, len(inputs)):
        feature_example = [1]*16
        result.append(feature_example)

    dictionary_list = []
    dictionary_start = [0.0]*30
    for i in range(0, 30):
        dict = {}
        dictionary_list.append(dict)

    labels = [0]*len(inputs)
    i = 0
    while i < len(inputs):
        result[i][0] = process(inputs[i][0], dictionary_list, dictionary_start, 0)
        result[i][1] = process(inputs[i][1], dictionary_list, dictionary_start, 1)
        result[i][2] = float(inputs[i][2])
        result[i][3] = process(inputs[i][5], dictionary_list, dictionary_start, 5)
        result[i][4] = float(inputs[i][6])
        result[i][5] = float(inputs[i][7])
        result[i][6] = process(inputs[i][11], dictionary_list, dictionary_start, 11)
        result[i][7] = float(inputs[i][13])
        result[i][8] = float(inputs[i][14])
        result[i][9] = process(inputs[i][18], dictionary_list, dictionary_start, 18)
        result[i][10] = process(inputs[i][20], dictionary_list, dictionary_start, 20)
        result[i][11] = process(inputs[i][22], dictionary_list, dictionary_start, 22)
        result[i][12] = float(inputs[i][25])
        result[i][13] = float(inputs[i][28])
        result[i][14] = float(inputs[i][29])
        result[i][15] = float(inputs[i][31])/20.0
        labels[i] = get_label_for_alcohol_comsumption(float(inputs[i][26]), float(inputs[i][27]))
        i += 1

    i = 0
    while i < 16:
        normalize_feature(result, i)
        i += 1
    return result, labels


inputs = get_inputs()
features, labels = process_input_files(inputs)
train_feature, train_label, test_feature, test_label = divide_dataset(features, labels)

model = SVC()
# model = DecisionTreeClassifier()
model.fit(train_feature, train_label)
result = model.predict(test_feature)

i = 0
sum = 0
total = len(result)
while i < total:
    if result[i] == test_label[i]:
        sum += 1
    i += 1
print float(sum*100.0)/float(total)