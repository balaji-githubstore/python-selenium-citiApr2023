from base.webdriver_wrapper import AutomationWrapper
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI(AutomationWrapper):
    def test_title(self):
        actual_title = self.driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record")
