from stock_exchange import *
from report import *
from sys import argv, exit
import getopt


def usage():
    print("Usage python3 scrap.py -s STOCK_EXCHANGE_TAG -d START_DATE\n")
    print("-d       set when we start to scrap data. The format of date must be YY::MM::DD\n")
    print("-h       print this output. This option can't be use with others\n")
    print("-s       define which stock exchange we want extract data\n")
    print("         NASDAQ; FTSE; SP-500; NIFTY; OTHER\n")


if __name__ == "__main__":
    generate_report = False

    try:
        opts, args = getopt.getopt(argv[1:], "s:d:h:g:v")
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
    elif opt == '-g':
        generate_report = True
    elif opt == '-v':
        start_date = arg
try:
    s = StockExchange(stock_exchange)
    s.get_historical_datas(start_date)
    s.create_csv()
    if generate_report == True:
        report = Report()
        report.generate_report(pd.read_csv(environ['CSV']))
except KeyError as e:
    print(f"The key {format(e)} not exist. Please check if you didn't make a mistake. You can use -h arg to see a list of stock exchange")
    exit(2)
