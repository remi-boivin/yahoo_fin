from datetime import date
from os import environ, getenv
from yahoo_fin import stock_info

class Report():
    
    def __init__(self, folder_timestamp):
        """ """
        self.folder_timestamp = folder_timestamp

    def generate_report(self, data):
        """ """
        report_file = f"datas/{folder_timestamp}/report.txt"
        f = open(report_file, 'w+')
        f.write(f"Start date: {data['date'][[data.index[0]][0]]}\nEnds at: {data['date'][[data.index[-1]][0]]}\n")
        f.write(f"{report_file} has : {len(data.index)} lines\n\n")
        f.close()