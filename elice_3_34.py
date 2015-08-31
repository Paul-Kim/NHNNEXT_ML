#elice_3_34.py
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import numpy as np
import pandas as pd
import elice_utils


def main():
    np.random.seed(108)

    # 1



    return draw_graph([noisy_circles, blobs])


def run_kmeans(X, num_clusters):
    # 2



    return kmeans


def run_DBScan(X, eps):
    # 3



    return dbscan


def draw_graph(datasets, n_clusters=2, eps=0.2, alg_name = ['KMeans', 'DBScan']):
    plot_num = 1

    elice_utils.draw_init()

    for dataset in datasets:
        # 4



        kmeans_result = run_kmeans(X, n_clusters)
        dbscan_result = run_DBScan(X, eps)

        for name, algorithm in zip(alg_name, [kmeans_result, dbscan_result]):
            elice_utils.draw_graph(X, algorithm, name, plot_num)
            plot_num += 1

    print(elice_utils.show_graph())

    return dbscan_result


if __name__ == '__main__':
    main()
