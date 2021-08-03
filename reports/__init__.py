from datetime import date
from os import environ
from yahoo_fin import stock_info

class Report():
    
    def __init__(self):
        """ """

        pass

    def generate_report(self, data):
        """ """
        f = open("datas/report.txt", "w")
        f.write(f"Start date: {data['date'][[data.index[0]][0]]}\nEnds at: {data['date'][[data.index[-1]][0]]}\n")
        f.write(f"{environ['CSV']} as : {len(data.index)} lines\n\n")
        f.write(f"Exemple {environ['CSV']} contain: \n{data.describe()}\n")
        f.close()