import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.citibank.co.in/ssjsps/forgetuseridmidssi.jsp")

driver.find_element(By.LINK_TEXT,"select your product type").click()
driver.find_element(By.LINK_TEXT,"Credit Card").click()

#approach 1
# driver.find_element(By.ID,"bill-date-long").send_keys("10/11/2000")

#approach using js & webelement
ele1=driver.find_element(By.XPATH,"//input[@name='DOB']")
driver.execute_script("arguments[0].value='10/11/2000'",ele1)





time.sleep(5)