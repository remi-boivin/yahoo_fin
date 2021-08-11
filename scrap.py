from stock_exchange import *
from reports import *
from sys import argv, exit
from optparse import OptionParser
from os import getenv

def get_opts():
    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                    action="store_true", dest="verbose", default=False,
                    help="Increase output verbosity.")
    parser.add_option("-t", "--tickers",
                    default="ALL", dest="tickers",
                    help="Choose specific market tickers. (NASDAQ; FTSE; SP-500; NIFTY; ALL [default]).")
    parser.add_option("-d", "--start_date",
                    default="1970::01::01", dest="start_date",
                    help="Set the start date (format: YY::MM::DD, default is 1970::01::01).")
    parser.add_option("-c", "--concat",
                    action="store_true", dest="concat", default=False,
                    help="Concat all csv in datas/tmp into one csv. The output file is define by CSV env var.")
    return parser.parse_args()


if __name__ == "__main__":
    (options, args) = get_opts()
    print(f"Launching script with options : {options}")
    try:
        s = StockExchange(options.tickers)
        folder_timestamp = s.get_historical_datas(options.start_date)
        df = pd.DataFrame()
        if options.concat == True:
            s.create_csv()
        report = Report(folder_timestamp)
        try:
            df = pd.read_csv(getenv('CSV', 'datas/data.csv'))
            report.generate_report(df)
        except FileNotFoundError:
            s.create_csv()
            df = pd.read_csv(getenv('CSV', 'datas/data.csv'))
            report.generate_report(df)
            system(f"rm {getenv('CSV', 'datas/data.csv')}")
    except KeyError as e:
        print(f"The key {format(e)} not exist. Please check if you didn't make a mistake. You can use -h arg to see a list of stock exchange")
        exit(2)
