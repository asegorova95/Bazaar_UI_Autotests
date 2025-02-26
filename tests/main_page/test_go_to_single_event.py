import pytest
import allure
from pages.EventPage import EventPage
from pages.MainPage import MainPage


@allure.title("[Web][MainPage][EventsWidget] Переход к мероприятию")
@pytest.mark.usefixtures("setup")
class TestEventsPage:
    def test_go_to_single_event(self):
        driver = self.driver  # Берём браузер из фикстуры
        main_page = MainPage(driver)
        event_page = EventPage(driver)


        # Кликаем по баннеру с каруселью мероприятий
        main_page.click_event_banner()

        assert event_page.get_event_title(),"Заголовок мероприятия не найден - FAILED"