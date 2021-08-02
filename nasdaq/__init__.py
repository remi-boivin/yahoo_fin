from yahoo_fin import stock_info
import pandas as pd
import numpy as np

class Nasdaq():

    def __init__(self):
        """ """

        self.tickers_list = stock_info.tickers_nasdaq()
        self.tickers_list_data = pd.DataFrame()

    def get_historical_datas(self, date='01/01/1990'):
        """ """

        for data in self.tickers_list:
            try:
                try:
                    self.tickers_list_data = pd.concat(
                    [self.tickers_list_data, stock_info.get_data(data, date, index_as_date=True)])
                    nan_count = self.tickers_list_data.isna().sum()
                    if 0 not in nan_count:
                        print(f'You dropped\n {nan_count}\nNaN occurences')
                        self.tickers_list_data.dropna()
                except KeyError:
                    print('Key timestamp not found')
            except AssertionError:
                print('No data')

    def get_company(self, company):
        """" """

        new_df = self.tickers_list_data[(
            self.tickers_list_data.ticker == company.upper())]
        return new_df
