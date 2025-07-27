import pandas as pd

def get_performance_stats(symbol):
    return pd.DataFrame({
        'Date': ['2025-07-25', '2025-07-26'],
        'Signal': ['BUY', 'SELL'],
        'P/L': [1200, -800]
    })
