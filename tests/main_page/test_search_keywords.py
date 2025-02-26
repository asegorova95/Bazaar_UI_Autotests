import time

import pytest
import allure
from pages.MainPage import MainPage
from pages.SearchPage import SearchPage
from utils.BaseClass import BaseClass


@allure.title("[Desktop][MainPage][EventsWidget] Переход к Афише")
@pytest.mark.usefixtures("setup")
class TestSearchKeyword(BaseClass):
    def test_search_by_keywords(self):
        driver = self.driver  # Берём браузер из фикстуры
        main_page = MainPage(driver)
        search_page = SearchPage(self.driver)

        # Запоминаем старый заголовок ДО нажатия на поиск
        old_title = search_page.get_search_title()

        # Вводим ключевое слово в серчбар
        keyword = main_page.search_by_keyword()

        # Кликаем "Найти"
        main_page.click_search_button()
        search_page.wait_for_text_to_change(search_page.title_search_page, old_title)
        # Check search results
        assert keyword in search_page.get_search_title(), f"Ключевое слово '{keyword}' не найдено в title"
