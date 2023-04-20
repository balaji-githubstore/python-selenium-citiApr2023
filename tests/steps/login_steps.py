from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import assert_that


@given(u'I have browser with openemr page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demo.openemr.io/b/openemr/")


@when(u'I enter username as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "authUser").send_keys(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.ID, "clearPass").send_keys(text)


@when(u'I select language as "{text}"')
def step_impl(context, text):
    print("lan")


@when(u'I click on login')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, "#login-button").click()


@then(u'I should get access to portal with title as "{text}"')
def step_impl(context, text):
    assert_that(text).is_equal_to(context.driver.title)


@then(u'I should not get access portal with error as "{text}"')
def step_impl(context, text):
    print("lan")
