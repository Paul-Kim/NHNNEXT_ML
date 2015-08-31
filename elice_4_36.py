#elice_4_36.py
import pandas as pd
import numpy as np
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import sklearn.cross_validation
import elice_utils


def main():
    C = 1.0
    X, y = load_data()

    svc_linear = run_linear_SVM(X, y, C)
    svc_poly2 = run_poly_SVM(X, y, 2, C)
    svc_poly3 = run_poly_SVM(X, y, 3, C)
    svc_rbf = run_rbf_SVM(X, y, C)

    elice_utils.draw_graph(X, y, svc_linear, svc_poly2, svc_poly3, svc_rbf)


def load_data():
    # 1
    blobs = pd.read_csv('blobs.csv')
    blobs = blobs.set_index('index')

    return X, y


def run_linear_SVM(X, y, C):
    # 2


    return svc_linear


def run_poly_SVM(X, y, degree, C):
    # 3


    return svc_poly


def run_rbf_SVM(X, y, C, gamma=0.7):
    # 4


    return svc_rbf


if __name__ == "__main__":
    main()
