import pandas as pd

def get_market_overview():
    return pd.DataFrame({
        'Symbol': ['NIFTY', 'BANKNIFTY'],
        'Change': [0.55, -0.45],
        'Volume': [12345, 23456]
    })
