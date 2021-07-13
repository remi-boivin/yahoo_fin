from datetime import date
from os import environ
class Report():
    
    def __init__(self):
        """ """

        pass

    def generate_report(self, data):
        """ """

        f = open("report.txt", "a+")
        f.write(f"\n\n{date.today()} Changelog:\n\n")
        f.write(f"{environ['CSV']} as : {len(data.tickers_list_data.index)} lines\n\n")
        for company in data.tickers_list:
            f.write(f"{company} has nb row: #{len(data.get_company(company).index)}\n")
        f.close()