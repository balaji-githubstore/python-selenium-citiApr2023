import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://nasscom.in/")


actions=webdriver.ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Membership']")).perform()

driver.find_element(By.XPATH,"//a[text()='Members Listing']").click()