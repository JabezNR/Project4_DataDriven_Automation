import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from DataDriven_Automation import ExcelUtilities
from selenium.webdriver.support.select import Select

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
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.implicitly_wait(120)

file="C:\\Excel\\fixed_deposit.xlsx"
rows=ExcelUtilities.getRowCount(file,"Sheet1")
try:
    for r in range(2,rows+1):
        """# Read the data from Excel"""
        Principle=ExcelUtilities.readData(file,"Sheet1",r,1)
        Rate_of_interest=ExcelUtilities.readData(file,"Sheet1",r,2)
        period1=ExcelUtilities.readData(file,"Sheet1",r,3)
        period2=ExcelUtilities.readData(file, "Sheet1", r, 4)
        Frequency=ExcelUtilities.readData(file, "Sheet1", r, 5)
        Maturity_value=ExcelUtilities.readData(file, "Sheet1", r, 6)

        driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(Principle)
        driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(Rate_of_interest)
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
        Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")).select_by_visible_text(period2)
        Select(driver.find_element(By.XPATH, "//select[@id='frequency']")).select_by_visible_text(Frequency)

        driver.find_element(By.XPATH,"//div[@class='cal_div']//a[1]/img").click()

        maturity=driver.find_element(By.CSS_SELECTOR,"span[id='resp_matval'] strong").text

        if float(Maturity_value)==float(maturity):
            print("Test Passed")
            ExcelUtilities.writeData(file,"Sheet1",r,8,"Passed")
            ExcelUtilities.fillGreenColour(file,"Sheet1",r,8)
            time.sleep(2)
        else:
            print("Test Failed")
            ExcelUtilities.writeData(file, "Sheet1", r, 8, "Failed")
            ExcelUtilities.fillRedColour(file, "Sheet1", r, 8)
            time.sleep(2)

        driver.find_element(By.CSS_SELECTOR,"img[class='PL5']").click()
except:
    print ("failed")
driver.quit()




