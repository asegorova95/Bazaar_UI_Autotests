from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EventPage:
    event_title = (By.CLASS_NAME, "PosterDetail_info_header_title__Tl4uS")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator,
                         timeout=10):  # Ждать, пока элемент станет кликабельным, и только потом вернуть его.
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def get_event_title(self):
        return self.wait_for_element(self.event_title)
