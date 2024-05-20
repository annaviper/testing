from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAmazonBestSellers:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.amazon.com/')

    def test_amazon_best_sellers_items(self):
        best_sellers_xpath = "//div[@id='nav-xshop']/a[contains(@href, 'bestsellers')]"
        self.driver.find_element(By.XPATH, best_sellers_xpath).click()
        tabs = self.driver.find_elements(By.XPATH, "//div[@id='zg_tabs']//li")
        tabs_length = len(tabs)
        assert tabs_length == 5, f"Expected '5', but actual length '{tabs_length}'"

    def teardown_method(self):
        self.driver.quit()
