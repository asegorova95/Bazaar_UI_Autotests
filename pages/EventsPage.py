from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EventsPage:
    events_calendar = (By.CLASS_NAME, "calendar_container__303lB")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10): # Ждать, пока элемент станет кликабельным, и только потом вернуть его.
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
    def check_event_calendar(self):
        return self.wait_for_element(self.events_calendar)
