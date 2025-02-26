import allure
import pytest
from pages.MainPage import MainPage


@allure.title("Проверка наличия title h1")
@pytest.mark.usefixtures("setup")
class TestHomePage:
    def test_title(self):
        home_page = MainPage(self.driver)

        # Проверяем h1 на главной
        homepage_title = home_page.get_title()

        assert "BAZAAR" in homepage_title
