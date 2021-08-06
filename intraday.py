import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import threading
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from os import mkdir, path
import datetime

def get_tickers():
    tickers_list = []

    sleep(1)
    for i in range(30):
        tickers = driver.find_element(By.XPATH, f'/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/section/div/table/tbody/tr[{i + 1}]/td[1]/a')
        print(f"Eleement = {tickers.get_attribute('innerHTML')}")
        tickers_list.append(tickers.get_attribute('innerHTML'))
        i += 1
    return tickers_list

def get_cac40():
    sleep(5)
    print("sleep end")
    try:
        elem = driver.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]')
        print(f"Eleement = {elem}")
        elem.send_keys("CAC 40")
        elem.send_keys(Keys.RETURN)
        sleep(5)
        # elem = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
        # print(f"Eleement = {elem.get_attribute('innerHTML')}")
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/ul/li[6]/a/span').click()
        # selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: /html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/ul/li[6]/a/span

        tickers = get_tickers()
        for ticker in tickers:
            print("sleep boucle end")
            try:
                elem = driver.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]')
                elem.send_keys(ticker)
                elem.send_keys(Keys.RETURN)
                sleep(5)
                elem = driver.find_element(By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')
                try:
                    df = pd.concat(
                        [pd.DataFrame(data=elem.get_attribute('innerHTML'),index=[datetime.datetime.now()], columns=['value']), pd.read_csv(f"datas/{ticker}/{ticker}.csv", index_col=0)])
                    print(f"ticker = {ticker} Element = {df}")
                    df.to_csv(f"datas/{ticker}/{ticker}.csv")
                except FileNotFoundError:
                    if not path.exists(f'datas/{ticker}'):
                        mkdir(f"datas/{ticker}")
                    df = pd.DataFrame(data=elem.get_attribute('innerHTML'),index=[datetime.datetime.now()], columns=['value'])
                    df.to_csv(f"datas/{ticker}/{ticker}.csv")
            except NoSuchElementException:
                print(f'No data for {ticker}')
    except NoSuchElementException:
        print('no form')

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")

while (True):
    driver = webdriver.Firefox()
    t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
    t.start()
    get_cac40()
    sleep(60)
    driver.close()