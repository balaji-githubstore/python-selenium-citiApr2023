import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
#example for javascript alert handling
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm")

driver.find_element(By.XPATH,"//img[@alt='Go']").click()

#wait for alert is present
wait=WebDriverWait(driver,40)
wait.until(expected_conditions.alert_is_present())

alert_text=driver.switch_to.alert.text
print(alert_text)

driver.switch_to.alert.accept()
time.sleep(5)