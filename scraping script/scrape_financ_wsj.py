# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 15:27:14 2020

@author: Leandra S.
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

#point to path where your specific chromedriver is located
chrome_driver = os.path.abspath('../../chromedriver.exe')
browser = webdriver.Chrome(chrome_driver)

ticker_dat = pd.read_csv(os.path.abspath('../proc files/sp500.csv'))
ticker_list = ticker_dat['Symbol'].tolist()

#ticker = "AMZN"
#domain = "https://www.wsj.com/market-data/quotes/" + ticker + "/financials/quarter/income-statement"
#
#browser.get(domain)
#
##elements = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table.cr_dataTable tbody tr td[class]:nth-child(1)')))
#elements = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'table.cr_dataTable')))
#for element in elements:
#    print(element.text)
    
#df = pd.read_html(browser.page_source)[0]
#print(df.head())

incom_dat = []

for ticker in ticker_list:
    
        print(ticker)
        url = "https://www.wsj.com/market-data/quotes/" + ticker + "/financials/quarter/income-statement"
        browser.get(url)
        
        try:
            df = pd.read_html(browser.page_source)[0]
        except:
            continue
        
        df['Ticker Symbol'] = ticker
        df = df.rename(columns={df.columns[0]: 'Measure'})
        incom_dat.append(df)

        
income_statements = pd.concat(incom_dat)
cols_first = ['Ticker Symbol', 'Measure']
new_cols = cols_first + income_statements.columns.drop(cols_first).tolist()
income_statements = income_statements[new_cols]
