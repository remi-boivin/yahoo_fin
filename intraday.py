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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
import pandas as pd
from os import mkdir, path
import datetime

def get_tickers():
    tickers_list = []
    wait = WebDriverWait(driver, 5)
    elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yfin-usr-qry"]')))
    elem.send_keys("cac 40")
    elem.send_keys(Keys.RETURN)
    wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/section/div/ul/li[6]/a/span'))).click()    
    for i in range(30):
        tickers = wait.until(EC.visibility_of_element_located((By.XPATH, f'/html/body/div[1]/div/div/div[1]/div/div[3]/div[1]/div/div[1]/section/section/div/table/tbody/tr[{i + 1}]/td[1]/a')))
        print(f"Eleement = {tickers.get_attribute('innerHTML')}")
        tickers_list.append(tickers.get_attribute('innerHTML'))
        i += 1
    return tickers_list

def get_cac40(tickers):
    wait = WebDriverWait(driver, 10)
    try:
        for ticker in tickers:
            print("sleep boucle end")
            try:
                elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="yfin-usr-qry"]')))
                elem.send_keys(ticker)
                elem.send_keys(Keys.RETURN)
                try:
                    elem = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]')))
                    try:
                        df = pd.concat(
                            [pd.DataFrame(data=elem.get_attribute('innerHTML'),index=[datetime.datetime.now()], columns=['value']), pd.read_csv(f"datas/{ticker}/{ticker}.csv", index_col=0)])
                        print(f"ticker = {ticker} Element = {df}")
                        df.to_csv(f"datas/{ticker}/{ticker}.csv")
                    except FileNotFoundError:
                        if not path.exists(f'datas/{ticker}'):
                            mkdir(f"datas/{ticker}")
                        df = pd.DataFrame(data=elem.get_attribute('innerHTML'),index=[datetime.datetime.now()], columns=['value'])
                        print(f"ticker = {ticker} Element = {df}")
                        df.to_csv(f"datas/{ticker}/{ticker}.csv")
                except NoSuchElementException:
                    t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
                    t.start()
            except TimeoutException:
                print(f'No data for {ticker}')
                t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
                t.start()
        
            t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
            t.start()
    except TimeoutException:
        print('no form')
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Firefox()

t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
t.start()
tickers = get_tickers()
t = threading.Thread(target=driver.get, args=('https://fr.finance.yahoo.com/lookup',))
t.start()
while (True):
    get_cac40(tickers)
    sleep(10)