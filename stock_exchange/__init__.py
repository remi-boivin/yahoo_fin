from os import getenv, system, mkdir, path
from yahoo_fin import stock_info
import pandas as pd
import numpy as np
import glob
from datetime import datetime
import time


class StockExchange():

    def __init__(self):
        ticker_tag = 'ALL'
        self.__init__(ticker_tag)


    def __init__(self, ticker_tag):
        """ """
        tickers = {
            'SP-500': stock_info.tickers_sp500,
            'NASDAQ': stock_info.tickers_nasdaq,
            'FTSE': stock_info.tickers_ftse250,
            'NIFTY': stock_info.tickers_nifty50,
            'ALL': stock_info.tickers_other,
        }
        self.ticker_tag = ticker_tag
        self.tickers_list = tickers[ticker_tag]()
        self.tickers_list_data = pd.DataFrame()


    def get_historical_data(self, date='01/01/1990'):
        folder_name = int(time.time())
        for data in self.tickers_list:
            try:
                try:
                    self.tickers_list_data = stock_info.get_data(
                        data, date, index_as_date=False)
                    nan_count = self.tickers_list_data.isna().sum()
                    if nan_count != 0:
                        print(f"{nan_count.sum()} NaN occurrences has been dropped")
                        self.tickers_list_data.dropna()
                    if not path.exists(f'data/{folder_name}'):
                        mkdir(f"data/{folder_name}/")
                    if not path.exists(f'data/{folder_name}/{self.ticker_tag}'):
                        mkdir(f"data/{folder_name}/{self.ticker_tag}")
                    if not path.exists(f'data/{folder_name}/{self.ticker_tag}/{data}'):
                        mkdir(f"data/{folder_name}/{self.ticker_tag}/{data}")
                    self.tickers_list_data.to_csv(f"data/{folder_name}/{self.ticker_tag}/{data}/{data}.csv", index=False)
                except KeyError:
                    print('Key Timestamp not found')
            except AssertionError:
                print(f'The ticker {data} has no data')
        return folder_name

    def create_csv(self):
        csvfiles = []
        csv = pd.DataFrame()

        for file in glob.glob("data/*/*/*.csv"):
            csv = pd.concat(
                [csv, pd.read_csv(f"{file}", index_col=0)])
            csv.to_csv(getenv('CSV', 'data/data.csv'))
