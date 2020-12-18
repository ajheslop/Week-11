from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time
import unittest

class PollsDjangoPage(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """Assert that title of page says 'polls'."""
        self.browser.get('127.0.0.1:8000/polls')
        self.assertIn('polls', self.browser.title)

    def tearDown(self):
        self.browser.quit()
       
    def test_selectwhatsage(self):
        # Test name: select whats age
        # Step # | name | target | value
     # 1 | open | /polls/ | 
        self.driver.get("http://localhost:8000/polls/")
        # 2 | setWindowSize | 752x824 | 
        self.driver.set_window_size(752, 824)
        # 3 | click | linkText=What's your age? | 
        self.driver.find_element(By.LINK_TEXT, "What\'s your age?").click()
        # 4 | click | id=choice | 
        self.driver.find_element(By.ID, "choice").click()
        # 5 | click | css=input:nth-child(11) | 
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(11)").click()
if __name__ == '__main__':
    unittest.main(verbosity=2)