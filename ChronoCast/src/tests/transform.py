import numpy as np
import pandas as pd

    
def first_difference(df: pd.DataFrame):
    '''calcultes the first difference of close price'''
    
    data = df.copy()
    
    data["Differenced"] = data["Close"].diff()

    return data

def second_difference(df: pd.DataFrame):
    '''calculate the second difference of price ( stock )'''

    data = df.copy()

    data["Second_Difference"] = (
        data["Close"]
        .diff()
        .diff()
    )

    return data


def log_transform(df: pd.DataFrame):
    '''impliment log transformation to the stock price'''

    data = df.copy()

    data["Log_Close"] = np.log(data["Close"])

    return data