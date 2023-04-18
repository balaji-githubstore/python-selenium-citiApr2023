import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://nasscom.in/")

window_size=driver.get_window_size()
print(window_size)

ele_size=driver.find_element(By.XPATH,"//a[text()='Membership']").size
print(ele_size)

ele_loc=driver.find_element(By.XPATH,"//a[text()='Membership']").location
print(ele_loc)
print(ele_loc["x"])
print(ele_loc["y"])
actions = webdriver.ActionChains(driver)
actions.move_by_offset(ele_loc["x"],ele_loc["y"]).perform()