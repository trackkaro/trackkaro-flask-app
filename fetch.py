import yfinance as yf
import datetime


def get_data_yf(ticker):
    # getting current date
    info = yf.Ticker(ticker).info
    info_keys = info.keys()
    try:

        data = dict()
        data['ticker'] = ticker
        data['previousClose'] = info['previousClose']
        data['currency'] = info['currency']
        data['fetchTime'] = datetime.datetime.utcnow()
        data['longName'] = info['longName'] if 'longName' in info_keys else data['shortname']
        data['market'] = info['market'] if 'market' in info_keys else 'unavailable'
        data['quoteType'] = info['quoteType'] if 'quoteType' in info_keys else 'unavailable'

    except Exception as e:
        return False
    return data
