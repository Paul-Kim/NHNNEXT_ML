#elice_4_44.py
import pandas as pd
import numpy as np
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import sklearn.cross_validation
import sklearn.lda
import elice_utils


def main():
    C = 1.0

    X, y = load_data()

    pca, X_pca = run_PCA(X, 2)
    lda, X_lda = run_LDA(X, y, 2)

    svc_linear_pca = run_linear_SVM(X_pca, y, C)
    svc_rbf_pca = run_rbf_SVM(X_pca, y, C)

    svc_linear_lda = run_linear_SVM(X_lda, y, C)
    svc_rbf_lda = run_rbf_SVM(X_lda, y, C)

    elice_utils.draw_graph(X_pca, X_lda, y, svc_linear_pca, svc_rbf_pca, svc_linear_lda, svc_rbf_lda)
    print(elice_utils.show_graph())


def load_data():
    # 1

    return feature_df, class_df


def run_PCA(dataframe, num_components):
    # 2

    return pca, pca_array


def run_LDA(X, y, num_components):
    # 3

    return lda, lda_array


def run_linear_SVM(X, y, C):
    # 4

    return svc_linear


def run_rbf_SVM(X, y, C, gamma=0.7):
    # 5

    return svc_rbf


if __name__ == "__main__":
    main()
