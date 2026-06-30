import pandas as pd 

def add_indicator(df: pd.DataFrame) -> pd.DataFrame:
    ''' Adds indicators such as SMA, EMA, Returns, and Volatility '''
    df = df.copy() 
    
    # Simple Moving Average
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean() 
    
    # Exponential Moving Average
    df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean()
    
    df['Daily_Return'] = df['Close'].pct_change()
    df['Cumulative_Return'] = (1 + df['Daily_Return'].fillna(0)).cumprod() - 1 
    
    # Rolling Volatility
    df["Rolling_Volatility"] = (
        df["Daily_Return"]
        .rolling(30)
        .std()
        * (252 ** 0.5)
    )
    
    return df
