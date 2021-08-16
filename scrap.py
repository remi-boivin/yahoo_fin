from stock_exchange import *
from reports import *
from sys import argv, exit
from optparse import OptionParser
from os import getenv
import logging

def get_opts():
    parser = OptionParser()
    parser.add_option("-v", "--verbose",
                    action="store_true", dest="verbose", default=False,
                    help="Increase output verbosity.")
    parser.add_option("-t", "--tickers",
                    default="ALL", dest="tickers",
                    help="Choose specific market tickers. (NASDAQ; FTSE; SP-500; NIFTY; ALL [default]).")
    parser.add_option("-d", "--start_date",
                    default="01/01/1970", dest="start_date",
                    help="Set the start date (format: DD/MM/YY, default is 01/01/1970).")
    parser.add_option("-c", "--concat",
                    action="store_true", dest="concat", default=False,
                    help="Concat all csv in data/tmp into one csv. The output file is define by CSV env var.")
    return parser.parse_args()

def set_log_level(verbose):
    if verbose:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)


if __name__ == "__main__":
    (options, args) = get_opts()
    set_log_level(options)
    print(f"Launching script with options : {options}")
    try:
        s = StockExchange(options.tickers)
        folder_timestamp = s.get_historical_data(options.start_date)
        df = pd.DataFrame()
        if options.concat == True:
            s.create_csv()
        report = Report(folder_timestamp)
        try:
            df = pd.read_csv(getenv('CSV', 'data/data.csv'))
            report.generate_report(df)
        except FileNotFoundError:
            s.create_csv()
            df = pd.read_csv(getenv('CSV', 'data/data.csv'))
            report.generate_report(df)
            system(f"rm {getenv('CSV', 'data/data.csv')}")
    except KeyError as e:
        logging.error(f"The key {format(e)} not exist. Please check if you didn't make a mistake. You can use -h arg to see a list of stock exchange")
        exit(2)
