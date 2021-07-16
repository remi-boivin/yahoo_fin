from datetime import date
from os import environ
from yahoo_fin import stock_info
import datas

class Report():
    
    def __init__(self):
        """ """

        pass

    def generate_report(self, data):
        """ """
        f = open("report.txt", "a+")
        f.write(f"\n\n{date.today()} Changelog:\n\n")
        f.write(f"{environ['CSV']} as : {len(data.index)} lines\n\n")
        f.write(f"Exemple {environ['CSV']} contain: \n{data.describe()}\n")
        f.close()