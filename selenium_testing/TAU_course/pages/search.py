from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:

	def __init__(self, browser):
		self.browser = browser
		self.URL = 'https://www.duckduckgo.com'
		self.search_input = (By.NAME, "q")

	def load(self):
		self.browser.get(self.URL)

	def search(self, phrase):
		search_input = self.browser.find_element(*self.search_input)
		search_input.send_keys(phrase)
		search_input.send_keys(Keys.ENTER)
