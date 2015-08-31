#elice_3_27_solution.py
import sklearn.decomposition
import numpy as np
import pandas as pd
import elice_utils

def main():
    df = input_data()

    # 2
    pca, pca_array = run_PCA(df, 1)

    # 4
    print(elice_utils.draw_toy_example(df, pca, pca_array))

def input_data():
    # 1
    num = (int)(input().strip())
    
    X = []
    Y = [] 
    for i in range(0, num):
        point = input().strip().split()
        X.append(float(point[0]))
        Y.append(float(point[1]))
    
    df = pd.DataFrame({'x': X, 'y': Y})
    return df

def run_PCA(dataframe, num_components):
    # 2
    pca = sklearn.decomposition.PCA(num_components)
    pca.fit(dataframe)
    pca_array = pca.transform(dataframe)
    
    return pca, pca_array

if __name__ == '__main__':
    main()