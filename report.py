from reports import *
from os import getenv
import pandas as pd

if __name__ == "__main__":
    reports = Report()
    reports.generate_report(pd.read_csv(getenv('CSV', 'datas/data.csv'))  )
