from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAmazonCart:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.amazon.com/')

    def test_amazon_cart_number_is_0(self):
        cart_number = self.driver.find_element(By.ID, 'nav-cart-count').text
        assert cart_number == '0'

    def test_amazon_cart_is_empty(self):
        self.driver.find_element(By.ID, 'nav-cart').click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text = "Your Amazon Cart is empty"
        assert expected_text == actual_text, f"Expected '{expected_text}', actual text '{actual_text}'"

    def teardown_method(self):
        self.driver.quit()
