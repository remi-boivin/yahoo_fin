from yahoo_fin import stock_info
import pandas as pd
import numpy as np

class Data():

    def __init__(self):
        """ """

        self.tickers_list = ["nflx"]#stock_info.tickers_sp500()
        self.tickers_list_data = pd.DataFrame()

    def get_historical_datas(self, date='07/07/2021'):
        """ """

        for data in self.tickers_list:
            self.tickers_list_data = pd.concat(
                [self.tickers_list_data, stock_info.get_data(data, date, index_as_date=True)])
        nan_count = self.tickers_list_data.isna().sum()
        if 0 in nan_count:
            print(f'You dropped\n {nan_count}\nNaN occurences')
            self.tickers_list_data.dropna()

    def get_company(self, company):
        """" """

        new_df = self.tickers_list_data[(
            self.tickers_list_data.tickner == company.upper())]
        return new_df
