from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

	# Web Elements. Could also be added to __init__ method.
	SEARCH_INPUT = (By.NAME, 'q')
	RESULT_LINKS = (By.CSS_SELECTOR, 'result-title-a')

	def __init__(self, browser) -> None:
		self.browser = browser

	def search_input_value(self) -> str:
		search_input = self.browser.find_element(*self.SEARCH_INPUT)
		value = search_input.get_attribute('value')
		return value

	def result_link_titles(self) -> list:
		links = self.browser.find_elements(*self.RESULT_LINKS)
		titles = [link.text for link in links]
		return titles

	def title(self) -> str:
		return self.browser.title
