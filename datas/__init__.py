from yahoo_fin.stock_info import *
import pandas as pd


class Data():

    def __init__(self, sp_500):
        """ """

        self.sp_500 = sp_500
        self.sp_500_data = pd.DataFrame()

    def get_historical_datas(self, date='07/07/2021'):
        """"""

        for data in self.sp_500:
            self.sp_500_data = pd.concat(
                [self.sp_500_data, get_data(data, date, index_as_date=True)])
        self.sp_500_data.dropna()

    def get_company(self, company):
        new_df = self.sp_500_data[(self.sp_500_data.ticker == company.upper())]
        return new_df
