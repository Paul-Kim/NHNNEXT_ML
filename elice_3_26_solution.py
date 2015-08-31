#elice_3_26_solution.py
import numpy as np
import pandas as pd

def main():
    do_exercise()

def do_exercise():
    # 1
    aapl_bars = pd.read_csv("./AAPL.csv")
    
    #2
    date_index = aapl_bars.pop('Date')
    aapl_bars.index = pd.to_datetime(date_index)
    
            
    aapl_bars = aapl_bars[:]['1989':'2003-04']
    
    arr = []
    dict = {}
        
    for colum in aapl_bars:
        if(colum in ["Open", "Close", "Volume"]):
            arr = (aapl_bars.pop(colum))
            dict[colum] =  arr
    print(dict)
    
    df = pd.DataFrame(dict)
    return df

if __name__ == "__main__":
    main()