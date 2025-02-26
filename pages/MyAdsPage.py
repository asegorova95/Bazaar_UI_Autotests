from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAdsPage:
    open_myads = (By.XPATH, "//a[contains(@href, '/user/my-ads')]")
    # active_tab = (By.CSS_SELECTOR, '[data-testid="active"]')
    myads_title = (By.CLASS_NAME, "personal-account-layout_title__NZC0N")

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):  # Ждать, пока элемент станет кликабельным, и только потом вернуть его.
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def open_profile(self):
        return self.wait_for_element(self.open_myads).click()

    def get_title_myads(self):
        return self.wait_for_element(self.myads_title).text

