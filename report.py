from reports import *
from os import environ
import pandas as pd

if __name__ == "__main__":
    reports = Report()
    reports.generate_report(pd.read_csv(environ['CSV'])  )
