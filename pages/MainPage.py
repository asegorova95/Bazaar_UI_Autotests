
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_data.search_data import random_keyword
from utils.BaseClass import BaseClass


class MainPage(BaseClass):
    title = (By.CLASS_NAME, "index-page_title__TNXLA")
    event_button = (By.CSS_SELECTOR, '[data-testid="events_page_button"]')
    event_banner = (By.CSS_SELECTOR, '[data-testid="event_banner"]')
    search_bar = (By.CSS_SELECTOR,'[data-testid="search_field"]')
    search_button = (By.CSS_SELECTOR,'[data-testid="search_button"]')

    def __init__(self, driver):
        self.driver = driver
    def get_title(self):
        return self.driver.find_element(*MainPage.title).text

    def click_event_banner(self):
        return self.wait_for_element(self.event_banner, condition="clickable").click()

    def click_event_button(self):
        return self.wait_for_element(self.event_button, condition="clickable").click()

    def search_by_keyword(self):
        keyword = random_keyword
        self.wait_for_element(self.search_bar).send_keys(keyword)
        return keyword

    def click_search_button(self):
        return self.wait_for_element(self.search_button, condition="clickable").click()









