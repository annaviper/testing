import json
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.options import Options


"""The fixtures make the browser available to all 
classes and functions in the package"""


@pytest.fixture
def config(scope='session'):
	with open('config.json') as config_file:
		config = json.load(config_file)

	return config


@pytest.fixture
def browser(config, scope='function'):

	# Initialize WebDriver instance
	browser = config['browser']
	if browser == 'Firefox':
		b = selenium.webdriver.Firefox()
	elif browser == 'Chrome':
		b = selenium.webdriver.Chrome()
	elif browser == 'Headless Chrome':
		ops = selenium.webdriver.ChromeOptions()
		ops.add_argument('headless')
		b = selenium.webdriver.Chrome(options=ops)
	else:
		raise Exception(f"Browser {browser} is not supported.")

	# Setup stage, step 2: Make its calls wait up to 10 seconds for elements to appear
	b.implicitly_wait(10)

	# Return the webdriver instance for the setup
	yield b

	# Clean up: Quit the webdriver instance for the cleanup
	b.quit()
