from nifty import *
from os import environ

if __name__ == "__main__":
    data = Nifty()
    data.get_historical_datas('01/08/2001')
    data.tickers_list_data.to_csv(environ['CSV'])
