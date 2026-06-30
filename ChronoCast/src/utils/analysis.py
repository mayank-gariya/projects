import pandas as pd
import numpy as np

def rolling_statistics(df:pd.DataFrame ,  window: int = 30) -> pd.DataFrame:
    """
    Add rolling mean and rolling standard deviation.
    """
    
    df = df.copy()
    
    df['Rolling_Mean'] = (df['Close'].rolling(window=window).mean())
    df['Rolling_STD'] = (df['Close'].rolling(window=window).std())
    
    return df

def annualized_volatility(df: pd.DataFrame) -> float:
    """
    Calculate annualized volatility using daily returns.
    """
    
    if "Daily_Return" not in df.columns:
        raise ValueError('Daily Return is not present run "add_indicator" first')
    
    volatility = (df['Daily_Return'].std() * np.sqrt(252))
    
    return float(volatility)

def trend_strength(df: pd.DataFrame) -> float:
    """
    Calculate percentage price change across the selected period.
    """
    
    first_price = float(df['Close'].iloc[0])
    last_price = float(df["Close"].iloc[-1])
    
    return ((last_price - first_price) / first_price) * 100

def return_statistics(df: pd.DataFrame) -> dict:
    """
    Summary statistics of daily returns.
    """
    
    returns = df["Daily_Return"].dropna()
    
    return {
        "mean_return": float(returns.mean()),
        "median_return": float(returns.median()),
        "std_return": float(returns.std()),
        "max_return": float(returns.max()),
        "min_return": float(returns.min()),
    }

def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Summary statistics of OHLCV data.
    """

    return df.describe().round(2)
    
    

          
    