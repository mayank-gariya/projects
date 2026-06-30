from src.data.data_loader import get_stock_data
from src.utils.indicators import add_indicator


def load_processed_data(ticker, start_date, end_date):
    """
    Load stock data and apply standard preprocessing.
    """
    data = get_stock_data(
        ticker,
        start_date,
        end_date,
    )

    if data is None or data.empty:
        return None

    if data.columns.nlevels > 1:
        data.columns = data.columns.get_level_values(0)

    data = data.loc[:, ~data.columns.duplicated()]

    data = add_indicator(data)

    return data