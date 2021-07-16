from datas import *
from os import environ

if __name__ == "__main__":
    data = Data()
    data.get_historical_datas('01/01/2020')
    data.tickers_list_data.to_csv(environ['CSV'])
