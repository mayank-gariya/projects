import pandas as pd


def calculate_metrics(df: pd.DataFrame):

    latest_close = float(df["Close"].iloc[-1])
    previous_close = float(df["Close"].iloc[-2])

    daily_change = latest_close - previous_close
    daily_change_pct = (daily_change / previous_close) * 100

    return {
        "current_price": latest_close,
        "daily_change": int(daily_change),
        "daily_change_pct": daily_change_pct,
        "period_high": float(df["High"].max()),
        "period_low": float(df["Low"].min()),
        "average_volume": float(df["Volume"].mean()),
        "highest_volume": float(df["Volume"].max()),
        "trading_days": int(len(df)),
    }