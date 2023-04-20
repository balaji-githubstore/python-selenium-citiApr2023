import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I have browser with fb page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://facebook.com")



@when(u'I click on create new patient')
def step_impl(context):
    context.driver.find_element(By.PARTIAL_LINK_TEXT, "Create new").click()


@when(u'I fill the registration form')
def step_impl(context):
    context.driver.find_element(By.NAME, "firstname").send_keys(context.table[0]["firstname"])
    context.driver.find_element(By.NAME, "lastname").send_keys(context.table[0]["lastname"])
    context.driver.find_element(By.NAME, "reg_email__").send_keys(context.table[0]["mobile_number"])
    time.sleep(5)

@then(u'I should see succesful message as "registered"')
def step_impl(context):
   print("hi")