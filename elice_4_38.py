#elice_4_38.py
import pandas as pd
import numpy as np
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import sklearn.cross_validation
import matplotlib.pyplot as plt


def main():
    C_list = [0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0]

    X, y = load_data()

    # 2
    X = sklearn.preprocessing.scale(X)

    X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(X, y, test_size=0.2, random_state=0)

    for C in C_list:
        svc_rbf = run_rbf_SVM(X_train, y_train, C)

        # 5
        train_score = test_svm_models(?, ?, svc_rbf)
        test_score = test_svm_models(?, ?, svc_rbf)

        print('RBF with C=%5d:\tTrain Acc=%f\tTest Acc=%f' % (C, train_score, test_score))


def load_data():
    # 1


    return X, y


def run_rbf_SVM(X, y, C, gamma=0.7):
    # 3

    return svc_rbf


def test_svm_models(X_data, y_data, each_model):
    # 4

    return score_value


if __name__ == "__main__":
    main()
