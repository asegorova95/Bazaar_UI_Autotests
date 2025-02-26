from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.BaseClass import BaseClass


class SearchPage(BaseClass):
    product_page = (By.CLASS_NAME, "desktop-ad-card_title__8cPdO")
    title_search_page = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_text_to_change(self, locator, old_text, timeout=10):
        """Ожидаем, пока текст заголовка изменится с прошлого значения"""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text.strip() != old_text,
            message=f"Текст заголовка {locator} не изменился"
        )

    def get_search_title(self):
        return self.wait_for_element(self.title_search_page, condition="visible").text