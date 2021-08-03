from os import environ, system
from yahoo_fin import stock_info
import pandas as pd
import numpy as np
import glob


class StockExchange():

    def __init__(self, ticker_tag):
        """ """
        tickers = {
            'SP-500': stock_info.tickers_sp500,
            'NASDAQ': stock_info.tickers_nasdaq,
            'FTSE': stock_info.tickers_ftse250,
            'NIFTY': stock_info.tickers_nifty50,
            'OTHER': stock_info.tickers_other,
        }
        self.tickers_list = tickers[ticker_tag]()
        self.tickers_list_data = pd.DataFrame()

    def get_historical_datas(self, date='01/01/1990'):
        """ """

        for data in self.tickers_list:
            try:
                try:
                    self.tickers_list_data = stock_info.get_data(
                        data, date, index_as_date=True)
                    nan_count = self.tickers_list_data.isna().sum()
                    if 0 not in nan_count:
                        print(f'You dropped\n {nan_count}\nNaN occurences')
                        self.tickers_list_data.dropna()
                    self.tickers_list_data.to_csv(f"datas/tmp/{data}.csv")
                except KeyError:
                    print('Key Timestamp not found')
            except AssertionError:
                print('No data')

    def create_csv(self):
        csvfiles = []
        csv = pd.DataFrame()

        for file in glob.glob("datas/tmp/*.csv"):
            csv = pd.concat(
                [csv, pd.read_csv(f"{file}")])
        csv.to_csv(environ['CSV'])
        system("rm datas/tmp/*.csv")
