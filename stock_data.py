import yfinance as yf

def get_stock_data(ticker, period="6mo"):
    return yf.download(ticker, period=period)