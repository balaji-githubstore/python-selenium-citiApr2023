import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://netbanking.hdfcbank.com/netbanking/")

# //frame[@name='login_page']
# //frame[contains(@src,'RSNB')]

driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))

driver.find_element(By.NAME,"fldLoginUserId").send_keys("test123")
#click on continue
driver.find_element(By.LINK_TEXT,"CONTINUE").click()
driver.switch_to.default_content()

time.sleep(5)
driver.quit()