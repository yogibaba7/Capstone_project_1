
import pandas as pd 
import numpy as np 
import requests 
from bs4 import BeautifulSoup
import os 
import time 

# city = 'Gurgaon' # By There We Can Provide any City.
# pagenumber = 1 
# # User Agent
# headers = {
#     'authority': 'www.99acres.com',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'no-cache',
#     'dnt': '1',
#     'pragma': 'no-cache',
#     'referer': f'https://www.99acres.com/flats-in-{city}-ffid-page={pagenumber}',
#     'sec-ch-ua': '"Chromium";v="107", "Not;A=Brand";v="8"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/527.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
# }



# url = f'https://www.99acres.com/flats-in-{city}-ffid-page={pagenumber}'
# response = requests.get(url, headers=headers)
# #print(page)
# if response.status_code == 200:
#     print('connection sucessful')
# else:
#     print(f"Error: {response.status_code}")

# --------------------------------------------------------------------------------------------------

# Import libries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# path of webdriver
s = Service("C:/Users/Yogesh/Desktop/chromedriver.exe")


# This code is optional for solve automatically close chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])

chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

chrome_options.add_argument('start-maximized')
# ---------------------------------------------------------------------


driver = webdriver.Chrome(service=s,options=chrome_options)

City = "chandigarh"
pageNumber = 1

url = f'https://www.99acres.com/flats-in-{City}-ffid-page-{pageNumber}'
driver.get(url)

html = driver.page_source

pageSoup = BeautifulSoup(html,'html.parser')
#print(pageSoup.select_one('div[data-label="SEARCH"]'))

for soup in pageSoup.select_one('div[data-label="SEARCH"]'):
    print('---------------------------')
    print(soup.select('a.srpTuple__propertyName'))
        # Extract property name and property sub-name
    # try:
    #     property_name = soup.select_one('a.srpTuple__propertyName').text.strip()
    #             # Extract link
    #     link = soup.select_one('a.srpTuple__propertyName')['href']
    #     society = soup.select_one('#srp_tuple_society_heading').text.strip()
    #     print(society)
    # except:
    #     print('No')