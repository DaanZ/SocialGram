

import os
import time

import rootpath
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self, headless=True):
        self.driver_path = os.path.join(rootpath.detect(), "chromedriver.exe")
        self.headless = headless

    def process(self, url, xpath: str = None):
        """Handle incoming scrape requests."""
        print(f"Received scrape request for URL: {url}")
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")  # Run in headless mode
        driver = webdriver.Chrome(service=Service(self.driver_path), options=chrome_options)

        driver.get(url)
        time.sleep(3)  # Wait for the page to load
        if xpath:
            driver.find_element(By.XPATH, xpath).click()
            time.sleep(3)

        return driver

    def init_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver_path = os.path.join(rootpath.detect(), "core", "utils", "chromedriver.exe")
        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
        return driver


if __name__ == "__main__":

    videos = ["https://www.tiktok.com/@lisaoudijn/video/7427134905458445601",
              "https://www.tiktok.com/@lisaoudijn/video/7426378117796711713",
              "https://www.tiktok.com/@lisaoudijn/video/7426011059443551520",
              "https://www.tiktok.com/@lisaoudijn/video/7425645346988018976",
              "https://www.tiktok.com/@lisaoudijn/video/7421558433905642785",
              "https://www.tiktok.com/@lisaoudijn/video/7421194213053697313",
              "https://www.tiktok.com/@lisaoudijn/video/7420458276489383201",
              "https://www.tiktok.com/@lisaoudijn/video/7402625527103753504"]


    url = videos[0]

    xpath = '//*[@id="xgwrapper-4-7427134905458445601"]/video/source[1]'

    scraper = Scraper(headless=False)
    driver = scraper.process(url)

    elements = driver.find_elements(By.TAG_NAME, "source")
    print(len(elements))
    for element in elements:
        print(element.get_property("src"))

    time.sleep(100)

