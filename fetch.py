import yfinance as yf
import datetime


def get_data_yf(tickers):
    api_res = yf.Tickers(tickers).tickers
    tickers = tickers.upper().split()
    datalist = []

    for ticker in tickers:
        info = api_res[ticker].info
        info_keys = info.keys()
        try:
            data = dict()
            data['ticker'] = ticker
            data['previousClose'] = info['previousClose']
            data['currency'] = info['currency']
            data['fetchTime'] = datetime.datetime.utcnow()
            data['longName'] = info['longName'] if 'longName' in info_keys else info['shortName']
            data['market'] = info['market'] if 'market' in info_keys else 'unavailable'
            data['quoteType'] = info['quoteType'] if 'quoteType' in info_keys else 'unavailable'
            datalist.append(data)

        except Exception as e:
            print(str(e))
            return False

    return datalist
