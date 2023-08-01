from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import unittest

from dotenv import load_dotenv
load_dotenv(dotenv_path="D:\Comparison_scrape\env_variables\.env")

url = os.getenv("URL")
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
location = os.getenv("LOCATION")

class TestScrape(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        
    def test_crawl_credentials(self):
        driver = self.driver
        try:
            driver.get(url)
            driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
            driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            driver.find_element(By.XPATH, "//button[@class='btn login-btn']").click()     

            driver.find_element(By.XPATH, "//input[@type='password']").send_keys(location)
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
        except Exception as e:
            print(e)

    def test_crawl_store_names(self):
        pass


    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



