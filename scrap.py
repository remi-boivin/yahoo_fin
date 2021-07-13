from datas import *

if __name__ == "__main__":
    data = Data(tickers_sp500())
    data.get_historical_datas()
    data.sp_500_data.to_csv('finantials.csv')
    print(data.get_company('msft'))