from stock_exchange import *
from reports import *
from sys import argv, exit
import getopt


def usage():
    print("Usage python3 scrap.py -s STOCK_EXCHANGE_TAG -d START_DATE\n")
    print("-c       Concat all csv in data/tmp into one csv. The output file is define by CSV env var\n")
    print("-d       Set when we start to scrap data. The format of date must be YY::MM::DD. This arg is obligatory \n")
    print("-h       Print this output. This option can't be use with others\n")
    print("-r       Generate a report. The output file is define by CSV env var\n")
    print("-s       Define which stock exchange we want extract data. This arg is obligatory\n")
    print("         NASDAQ; FTSE; SP-500; NIFTY; OTHER\n")


if __name__ == "__main__":
    generate_report = False
    concat_csv = False

    try:
        opts, args = getopt.getopt(argv[1:], "s:d:hcr")
    except getopt.GetoptError:
        usage()
        exit(2)

for opt, arg in opts:
    if opt == '-h':
        usage()
        exit(0)
    elif opt == '-s':
        stock_exchange = arg
    elif opt == '-d':
        start_date = arg
    elif opt == '-r':
        generate_report = True
    elif opt == '-c':
        concat_csv = True

try:
    s = StockExchange(stock_exchange)
    s.get_historical_datas(start_date)
    df = pd.DataFrame()
    if concat_csv == True:
        s.create_csv()
    if generate_report == True:
        report = Report()
        print('ok')
        try:
            df = pd.read_csv(environ['CSV'])
            report.generate_report(df)
        except FileNotFoundError:
            s.create_csv()
            df = pd.read_csv(environ['CSV'])
            report.generate_report(df)
            system(f"rm {environ['CSV']}")
except KeyError as e:
    print(f"The key {format(e)} not exist. Please check if you didn't make a mistake. You can use -h arg to see a list of stock exchange")
    exit(2)
