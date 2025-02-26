import pytest
import allure
from pages.EventsPage import EventsPage
from pages.MainPage import MainPage


@pytest.mark.usefixtures("setup")
class TestEventsWidget:
    @allure.title("[Desktop][MainPage][EventsWidget] Переход к Афише")
    def test_go_to_single_event(self):
        driver = self.driver  # Берём браузер из фикстуры
        main_page = MainPage(driver)
        events_page = EventsPage(driver)

        # Кликаем по баннеру с текстом "Афиша"
        main_page.click_event_button()

        assert events_page.check_event_calendar(),"Календарь афиши не найден - FAILED"