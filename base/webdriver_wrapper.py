import pytest
from selenium import webdriver


class AutomationWrapper:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # below code runs before every test method
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://demo.openemr.io/b/openemr/index.php")
        yield
        # below code runs after every test method
        self.driver.quit()
