"""Setup and teardown methods."""

from selenium import webdriver


class WebdriveMethods():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
            self.driver.quit()