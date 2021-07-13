from yahoo_fin import stock_info
import pandas as pd


class Data():

    def __init__(self):
        """ """

        self.tickers_list = ['msft', 'nflx', 'amzn']
        # self.tickers_list = stock_info.tickers_sp500()
        self.tickers_list_data = pd.DataFrame()

    def get_historical_datas(self, date='07/07/2021'):
        """ """
        i = 0

        for data in self.tickers_list:
            self.tickers_list_data = pd.concat([self.tickers_list_data, stock_info.get_data(data, date, index_as_date=True)])
        if self.tickers_list_data.isnull().values.any() == True:
            print(f"You have deleted {i} values");
            i += 1
        self.tickers_list_data.dropna()
    
    def get_company(self, company):
        """" """
        
        new_df = self.tickers_list_data[(self.tickers_list_data.ticker == company.upper())]
        return new_df
