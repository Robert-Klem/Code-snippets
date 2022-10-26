from yfinance import Ticker


def highest_in_period(ticker: str, period: str) -> float:
    ticker_object = Ticker(ticker)
    info = ticker_object.info 
    history = ticker_object.history(period=period)
    high = list(history['High'])
    highest = max(high)
    print(highest)
    print(info)
    return highest

highest_in_period('AAPL', '1mo')

