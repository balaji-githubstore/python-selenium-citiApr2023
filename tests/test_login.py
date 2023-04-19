import pytest
from selenium.webdriver.common.by import By
from assertpy import assert_that

from base.webdriver_wrapper import AutomationWrapper
from utils.data_utils import DataSource


class TestLogin(AutomationWrapper):
    @pytest.mark.parametrize("username,password,expected_title", DataSource.test_valid_login)
    def test_valid_login(self, username, password, expected_title):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert_that(expected_title).is_equal_to(self.driver.title)

    @pytest.mark.parametrize("username,password,expected_error", DataSource.test_invalid_login)
    def test_invalid_login(self, username, password, expected_error):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        actual_error = self.driver.find_element(By.XPATH, "//*[contains(text(),'Invalid')]").text
        assert_that(actual_error).contains(expected_error)
