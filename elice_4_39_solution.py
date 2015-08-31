#elice_4_49_solution.py
import os
import pandas as pd
import numpy as np
import sklearn.decomposition
import sklearn.preprocessing
import sklearn.cluster
import scipy.spatial.distance

def main():
    # 1
    stocks_df, code_to_name = load_data()

    stocks_df = calculate_fluctuations(stocks_df)
    print(stocks_df)

def calculate_fluctuations(stocks_df):
    # 2 delete beloww 1400 days.
    for colum in stocks_df.columns:
        if(stocks_df[colum].count()<1400):
            stocks_df.drop(colum,1,inplace=True)
        else:
            fluc = []
            before = 0
            for price in stocks_df[colum].values:
                if(before == 0):
                    fluc.append(before)
                    before = price
                else:
                    fluc.append((price-before)/before)
                    before = price
            stocks_df[colum] = fluc
    # 3
        
    return stocks_df

def load_data():
    stocks_df = pd.read_csv("./stocks.csv")
    stocks_df = stocks_df.set_index('index')
    krx_listed_companies = pd.read_csv("./krx_listed_companies.csv")

    code_to_name = {}
    for code, name in zip(krx_listed_companies['Code'].values, krx_listed_companies['Name'].values):
        z_code = '0' * (6 - len(str(code))) + str(code)
        code_to_name[z_code] = name

    return stocks_df, code_to_name

if __name__ == "__main__":
    main()