import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
x=[]
driver = webdriver.Chrome()
driver.get("https://www.taifex.com.tw/cht/3/futContractsDate")
date=driver.find_element(By.ID,"queryDate")
tx=driver.find_element(By.ID,"commodityId")
button=driver.find_element(By.ID,"button")
#button3=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div/div[3]/form/table/tbody/tr[4]/td/input[2]")
tx.send_keys("臺股期貨")
button.click()  
time.sleep(0.05)
test=driver.find_element(By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/div/div[4]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[11]/div[1]/font").text
x.append(test)
while test is not None:
    button3=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/div[2]/div/div[3]/form/table/tbody/tr[4]/td/input[2]")
   
    button3.click()
    time.sleep(0.05)
    try:
        test=driver.find_element(By.XPATH,
            "/html/body/div[1]/div[4]/div[2]/div/div[4]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[11]/div[1]/font").text
    except:
        continue
    x.append(test)
    if driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[2]/div/div[4]/table/tbody/tr[1]/td/p/span[2]").text == "日期2020/06/10": 
        break
print(x)
x.reverse()
Lots = {'Lots': x} 
df = pd.DataFrame(x) 
df.to_csv('test.csv')