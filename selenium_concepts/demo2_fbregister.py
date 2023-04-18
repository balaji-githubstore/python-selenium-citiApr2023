import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
#wait for page load to complete
driver.get("https://www.facebook.com/")

driver.find_element(By.LINK_TEXT, "Create new account").click()

# enter firstname as john
driver.find_element(By.NAME,"firstname").send_keys("john")
#enter lastname as wick
driver.find_element(By.NAME,"lastname").send_keys("wick")

# 20 Nov 2000
select_day=Select(driver.find_element(By.ID,"day"))
select_day.select_by_visible_text("20")

select_month=Select(driver.find_element(By.ID,"month"))
select_month.select_by_visible_text("Nov")

#select year as 2000
select_year=Select(driver.find_element(By.XPATH,"//select[@title='Year']"))
select_year.select_by_visible_text("2000")

#click on custom radio button
driver.find_element(By.XPATH,"//input[@value='-1']").click()

#click on submit
driver.find_element(By.NAME,"websubmit").click()
time.sleep(5)