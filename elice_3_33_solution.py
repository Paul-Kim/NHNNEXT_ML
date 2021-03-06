#elice_3_33_solution.py
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import numpy as np
import pandas as pd
import elice_utils


def main():
    np.random.seed(108)

    # 1
    noisy_circles = pd.read_csv('noisy_circle.csv')
    noisy_circles = noisy_circles.set_index('index')
    blobs = pd.read_csv('blobs.csv')
    blobs = blobs.set_index('index')

    return draw_graph([noisy_circles, blobs])


def run_kmeans(X, num_clusters):
    # 2
    kmeans = sklearn.cluster.KMeans(num_clusters)
    kmeans.fit(X)

    return kmeans


def draw_graph(datasets, n_clusters=2, alg_name = 'KMeans'):
    plot_num = 1

    elice_utils.draw_init()

    for dataset in datasets:
        # 3
        Y = dataset.pop('0')
        X = np.array(dataset)
        kmeans_result = run_kmeans(X, n_clusters)

        elice_utils.draw_graph(X, kmeans_result, alg_name, plot_num)
        plot_num += 1

    print(elice_utils.show_graph())

    return kmeans_result


if __name__ == '__main__':
    main()