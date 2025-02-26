import logging
import inspect
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setup")
class BaseClass:
    def wait_for_element(self, locator, timeout=10, condition="visible"):
        conditions = {
            "visible": EC.visibility_of_element_located,
            "clickable": EC.element_to_be_clickable,
            "present": EC.presence_of_element_located
        }
        return WebDriverWait(self.driver, timeout).until(conditions[condition](locator))

    def select_option_by_text(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
