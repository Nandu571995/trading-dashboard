def generate_signals(symbol):
    return [{
        'type': 'BUY',
        'symbol': symbol,
        'reason': 'MACD crossover + OI spike',
        'confidence': 78
    }]
