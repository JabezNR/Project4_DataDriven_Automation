import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import mysql.connector

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("C:\Windows\chromedriver.exe")
    ops=Options()
    ops.add_argument("--disable-notifications")
    driver=webdriver.Chrome(service=ser_obj,options=ops)
    return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("C:\Windows\msedgedriver.exe")
    driver=webdriver.Edge(service=ser_obj)
    return driver
def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("C:\Windows\geckodriver.exe")
    driver=webdriver.Firefox(service=ser_obj)
    return driver

driver=chrome_setup()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
con=mysql.connector.connect(host="localhost",port="3306",user="root",passwd="root",database="learn")
cur=con.cursor()
cur.execute("select * from fdcal")
try:
    for row in cur:
        #read the data from sql
        principle=row[0]
        Rateofintrest =row[1]
        period1 =row[2]
        period2 =row[3]
        Frequency =row[4]
        MaturityValue =row[5]

        #find the elements in web page and enter the data
        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(principle)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(Rateofintrest)
        driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(period1)

        year=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
        year.select_by_visible_text(period2)

        SI=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
        SI.select_by_visible_text(Frequency)

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
        Result=driver.find_element(By.CSS_SELECTOR,"span[id='resp_matval'] strong").text

        #validation

        if float(MaturityValue)==float(Result):
            print("Test passed")
        else:
            print("Test Failed")
        driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
except:
    print("connection failed")
con.close()
driver.close()
