import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestAmazon:
    driver = ''
    search_words = ['dress', 'shoes', 'toys', 'books']

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.get('https://www.amazon.com/')

    @pytest.mark.parametrize("search_query", search_words)
    def test_amazon_search(self, search_query):
        # Search
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)

        # Validate search
        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
        assert expected_text == actual_text, f'Expected {expected_text}, actual text {actual_text}'

    def teardown_method(self):
        self.driver.quit()
