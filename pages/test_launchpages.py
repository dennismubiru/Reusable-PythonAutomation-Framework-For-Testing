import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class loadable:
    # @pytest.fixture
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def depart_from(self, departure):
        #self.driver.get("https://www.yatra.com/")
        #self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 17)
        departure = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@for='BE_flight_origin_city']")))
        # departure = wait.until(EC.element_to_be_clickable((By.XPATH, " ")))
        departure.click
        departure.send_keys(departure)
        departure.send_keys(Keys.Enter)

    def going_to(self, destination):

        self.wait = WebDriverWait(self.driver, 17)
        destination = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        destination.click
        time.sleep(4)
        destination.send_keys(destination)
        destination.send_keys(Keys.Enter)

    def departure_date(self, all_dates):
        all_dates = self.driver.find_element(By.ID, "//input[@id='BE_flight_origin_date']")
        for date in all_dates:
            if date.get_attribute("data-date") == all_dates:
                date.click()
                break
