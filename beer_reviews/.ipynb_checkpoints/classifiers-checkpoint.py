"""Classification"""
import json
import os
import pickle

import numpy as np
import torch
from joblib import dump, load
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# from scipy import spatial
from transformers import BertModel, BertTokenizer

# import random
# from random import shuffle


tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")


def cls_embedding(context):
    """embed each np in the list using its context"""
    context = context.lower()
    input_ids = tokenizer.encode(context, add_special_tokens=True)
    with torch.no_grad():
        last_hidden_states = model(torch.tensor([input_ids]))[0]

    # Retrieving the sentence [c][l]a[s]sification token's embedding
    cls_embedding = np.asarray(last_hidden_states[0])
    return cls_embedding[0]


def reader_(embeddings_path="6497_augmentations_num.dat", end_ix=-1):
    """X, y"""
    if os.path.exist(embeddings_path):
        with open(embeddings_path, "rb") as input_file:
            numerical_ = pickle.load(input_file)
        if end_ix == -1 or end_ix > len(numerical_):
            end_ix = len(numerical_)
        X = numerical_["X"][:end_ix]
        y = numerical_["y"][:end_ix]
        return X, y

    # Reading raw data and extracting CLS representation
    example_sents = json.load(open("training_set.json", encoding="utf-8"))
    if end_ix == -1 or end_ix > len(example_sents):
        end_ix = len(example_sents)
    X = []
    y = []

    for i in range(len(example_sents[:end_ix])):
        X.append(np.asarray(cls_embedding(example_sents[i]["sentence"])))
        if example_sents[i]["class"] == "Positive":
            y.append(1)
        else:
            y.append(0)
        # Saving emebddings
        with open(str(end_ix) + embeddings_path, "wb") as output_file:
            pickle.dump(X, output_file)

    # Putting it all together
    numerical_ = {"X": X, "y": y}
    with open(str(end_ix) + embeddings_path, "wb") as output_file:
        pickle.dump(numerical_, output_file)
    return X, y


def train_test():
    samples_ = json.load(open("training_set.json", encoding="utf-8"))

    X_test = []
    y_test = []
    for annotated_sample in samples_[:100]:
        X_test.append(cls_embedding(annotated_sample["sentence"]))
        if annotated_sample["class"] == "Positive":
            y_test.append(1)
        else:
            y_test.append(0)
    with open("num_TRAIN.dat", "wb") as output_file:
        pickle.dump({"X": X_test, "y": y_test}, output_file)
    return X_test, y_test


names = [
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    # "Gaussian Process", # TOO SLOW
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
    "QDA",
]

classifiers = [
    KNeighborsClassifier(2),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    # GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(hidden_layer_sizes=(512,), random_state=1, max_iter=len(X) * 100),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
]


metrics_ = {
    "accuracy_score": accuracy_score,
    "balanced_accuracy_score": balanced_accuracy_score,
    # "top_k_accuracy_score": top_k_accuracy_score,
    "average_precision_score": average_precision_score,
    "brier_score_loss": average_precision_score,
    "f1_score": f1_score,
    "log_loss": log_loss,
    "precision_score": precision_score,
    "recall_score": recall_score,
    "jaccard_score": jaccard_score,
    "roc_auc_score": roc_auc_score,
}


def experiments_(X, y):
    """Training& evaluation"""
    # Split the data; 75% training, 25% test
    if type(X[0]) != "numpy.ndarray":
        X = [np.asarray(x_) for x_ in X]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, stratify=y, random_state=1
    )

    results_dict = {}
    for name, clf in zip(names, classifiers):
        model_path = "models/" + name.replace(" ", "_") + ".joblib"
        if os.path.exists(model_path):
            # Loading pre-training models
            clf = load(model_path)
        else:
            # Training
            clf.fit(X_train, y_train)
            dump(clf, model_path)

        # Evatualtion
        # Saving evaluation results
        results_dict[name] = {}
        for metric_, func_ in metrics_.items():
            results_dict[name][metric_] = func_(y_test, clf.predict(X_test))
        with open(
            "results/bgTrain_smTest_results.json", "w", encoding="utf-8"
        ) as outfile:
            json.dump(results_dict, outfile, indent=4)


"""
Model:   Nearest Neighbors ,    Accuracy:  0.9907692307692307
_______________________________

Model:   Linear SVM ,   Accuracy:  0.9593846153846154
_______________________________

Model:   RBF SVM ,      Accuracy:  0.6098461538461538
_______________________________


######### Trained on regular data // Tested on augmented data #########

Model:   Nearest Neighbors ,    Accuracy:  0.7729230769230769
_______________________________

Model:   Linear SVM ,   Accuracy:  0.8221538461538461
_______________________________

Model:   RBF SVM ,      Accuracy:  0.5673846153846154
_______________________________



[('accuracy_score', 0.9907692307692307), ('balanced_accuracy_score', 0.9903882901475196), ('average_precision_score', 0.9857922768685978), ('brier_score_loss', 0.9857922768685978), ('f1_score', 0.9897610921501707), ('log_loss', 0.31882193471434633), ('precision_score', 0.9931506849315068), ('recall_score', 0.9863945578231292), ('jaccard_score', 0.9797297297297297), ('roc_auc_score', 0.9903882901475197)]

"""