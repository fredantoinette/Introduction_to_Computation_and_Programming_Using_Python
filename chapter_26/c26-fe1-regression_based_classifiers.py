"""
Write code to plot the ROC curve and compute the AUROC when the model built in 
the figure is tested on 200 randomly chosen competitors. Use that code to 
investigate the impact of the number of training examples (try varying it from 
10 to 1010 in increments of 50) on the AUROC.
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import sklearn.linear_model as sklm
import sklearn.metrics as skm


# Functions for evaluating classifiers

def accuracy(true_pos, false_pos, true_neg, false_neg):
    numerator = true_pos + true_neg
    denominator = true_pos + true_neg + false_pos + false_neg
    return numerator / denominator

def sensitivity(true_pos, false_neg):
    try:
        return true_pos / (true_pos + false_neg)
    except ZeroDivisionError:
        return float("nan")
    
def specificity(true_neg, false_pos):
    try:
        return true_neg / (true_neg + false_pos)
    except ZeroDivisionError:
        return float("nan")
    
def pos_pred_val(true_pos, false_pos):
    try:
        return true_pos / (true_pos + false_pos)
    except ZeroDivisionError:
        return float("nan")
    
def neg_pred_val(true_neg, false_neg):
    try:
        return true_neg / (true_neg + false_neg)
    except ZeroDivisionError:
        return float("nan")
    
def get_stats(true_pos, false_pos, true_neg, false_neg, 
              toPrint = True):
    accur = accuracy(true_pos, false_pos, true_neg, false_neg)
    sens = sensitivity(true_pos, false_neg)
    spec = specificity(true_neg, false_pos)
    ppv = pos_pred_val(true_pos, false_pos)
    if toPrint:
        print(" Accuracy =", round(accur, 3))
        print(" Sensitivity =", round(sens, 3))
        print(" Specificity =", round(spec, 3))
        print( " Pos. Pred. Val. =", round(ppv, 3))
    return (accur, sens, spec, ppv)


# Build examples and divide data into training and test sets

class Runner(object):
    def __init__(self, name, gender, age, time):
        self._name = name
        self._feature_vec = np.array([age, time])
        self._label = gender
        
    def feature_dist(self, other):
        return ((self._feature_vec - other._feature_vec)**2).sum()**0.5
    
    def get_time(self):
        return self._feature_vec[1]
    
    def get_age(self):
        return self._feature_vec[0]
    
    def get_label(self):
        return self._label
    
    def get_features(self):
        return self._feature_vec
    
    def __str__(self):
        return (f"{self._name}: {self.get_age()}, " +
                f"{self.get_time()}, {self._label}")
    
def build_marathon_examples(file_name):
    df = pd.read_csv(file_name)
    examples = []
    for index, row in df.iterrows():
        a = Runner(row["Name"], row["Gender"], row["Age"], row["Time"])
        examples.append(a)
    return examples

def divide_training_test_sets(examples):
    random.seed(0)
    sample_indices = random.sample(range(len(examples)), 200)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    return training_set, test_set

def divide_training_test_sets_2(examples):
    random.seed(0)
    sample_indices = random.sample(range(len(examples)), 200)
    training_set, test_set = [], []
    for i in range(len(examples)):
        if i in sample_indices:
            test_set.append(examples[i])
        else:
            training_set.append(examples[i])
    training_set_2 = {}
    for i in range(10, 1011, 50):
        random.seed(0)
        training_set_2[i] = random.sample(training_set, i)
    return training_set_2, test_set


# Use logistic regression to predict gender

def apply_model(model, test_set, label, prob = 0.5):
    # Create vector containing feature vectors for all test examples
    test_feature_vecs = [e.get_features() for e in test_set]
    probs = model.predict_proba(test_feature_vecs)
    true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
    for i in range(len(probs)):
        if probs[i][1] > prob:
            if test_set[i].get_label() == label:
                true_pos += 1
            else:
                false_pos += 1
        else:
            if test_set[i].get_label() != label:
                true_neg += 1
            else:
                false_neg += 1
    return true_pos, false_pos, true_neg, false_neg

examples = build_marathon_examples("bm_results2012.csv")
training, test = divide_training_test_sets(examples)

feature_vecs, labels = [], []
for e in training:
    feature_vecs.append([e.get_age(), e.get_time()])
    labels.append(e.get_label())
model = sklm.LogisticRegression().fit(feature_vecs, labels)


# Construct ROC curve and find AUROC

def build_ROC(model, test_set, label, title, plot = True):
    xVals, yVals = [], []
    for p in np.arange(0, 1, 0.01):
        true_pos, false_pos, true_neg, false_neg =\
            apply_model(model, test_set, label, p)
        xVals.append(1.0 - specificity(true_neg, false_pos))
        yVals.append(sensitivity(true_pos, false_neg))
    auroc = skm.auc(xVals, yVals)
    if plot:
        plt.plot(xVals, yVals)
        plt.plot([0, 1], [0, 1,], "--")
        plt.title(title + " (AUROC =" + 
                  str(round(auroc, 3)) + ")")
        plt.xlabel("1 - Specificity")
        plt.ylabel("Sensitivity")
    return auroc

build_ROC(model, test, "M", "ROC for Predicting Gender")
plt.show()


def plot_training_examples_auroc(examples):
    training_2, test_2 = divide_training_test_sets_2(examples)
    feature_vecs_dict, labels_dict, models_dict = {}, {}, {}
    for i in training_2.keys():
        for e in training_2[i]:
            if i in feature_vecs_dict:
                feature_vecs_dict[i].append([e.get_age(), e.get_time()])
            else:
                feature_vecs_dict[i] = [[e.get_age(), e.get_time()]]
            if i in labels_dict:
                labels_dict[i].append(e.get_label())
            else:
                labels_dict[i] = [e.get_label()]
        models_dict[i] = sklm.LogisticRegression().fit(feature_vecs_dict[i], labels_dict[i])
    auroc_dict = {} 
    for i in models_dict.keys(): 
        auroc_dict[i] = build_ROC(models_dict[i], test_2, "M", "", False)
    x = auroc_dict.keys()
    y = auroc_dict.values()
    plt.plot(x, y, "-o")
    plt.title("Impact of # Training Examples on AUROC")
    plt.xlabel("# Training Examples")
    plt.ylabel("AUROC")
    for i, j in zip(x, y):
        print(str(i) + ", " + str(round(j, 5)))
    plt.show()

plot_training_examples_auroc(examples)
