# This will get the results of the store

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os

from dotenv import load_dotenv
load_dotenv(dotenv_path = "D:\Comparison_scrape\env_variables\.env")

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
location = os.getenv("LOCATION")
url = os.getenv("URL")

def crawl_credentials(driver) -> None:
    """Login credentials"""
    driver.find_element(By.XPATH, "//input[@type='email']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@class='btn login-btn']").click()

    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(location)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

def crawl_store_names(driver) -> list:
    """Get store names"""
    wait = WebDriverWait(driver, 10)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='inpt_CUSTRECORD_IV_OR_STORE']"))).click()
    target_element = driver.find_elements(By.XPATH, "//div[@class='dropdownNotSelected']")
    my_list_of_store = [store.text for store in target_element if store.text != "- None -"]
    
    driver.quit()

    return my_list_of_store

def main(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

    crawl_credentials(driver)
    store_result = crawl_store_names(driver)

    # store the list of stores inside a notepad txt file
    with open("list_of_store.txt", "w") as file:
        for item in store_result:
            file.write(item + "\n")

    # return store_result
main(url)