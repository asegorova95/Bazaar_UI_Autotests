import pytest
from pages.MyAdsPage import MyAdsPage
from pages.AuthorizationForm import AuthorizationForm
import allure


@allure.title("[Web][LoginPopUp] Авторизация пользователя через номер телефона")
@pytest.mark.usefixtures("setup")
class TestLoginEmail:
    def test_login_email(self):
        driver = self.driver  # Берём браузер из фикстуры
        login_page = AuthorizationForm(driver)  # Создаём объект перед вызовом метода
        my_ads_page = MyAdsPage(driver)

        # Открываем форму авторизации в хедере
        login_page.login_popup()

        # Выбираем форму ввода номера телефона
        login_page.select_phone_tab()

        # Очищаем форму
        login_page.phone_input_clean()
        login_page.phone_input_clean()

        # Вводим логин
        login_page.login_phone()

        # Кликаем "Войти"
        login_page.sing_in()

        # Вводим пароль
        login_page.input_password_phone()

        # Login
        login_page.sing_in()

        # Go to MyAdsPage
        my_ads_page.open_profile()

        # Check Auth
        ads_title = my_ads_page.get_title_myads()

        assert "Мои объявления" or "My Ads" in ads_title
