import pytest
from pages.MyAdsPage import MyAdsPage
from pages.AuthorizationForm import AuthorizationForm
import allure


@allure.title("[Web][LoginPopUp] Авторизация пользователя через почту")
@pytest.mark.usefixtures("setup")
class TestLoginEmail:
    def test_login_email(self):
        driver = self.driver # Берём браузер из фикстуры
        login_page = AuthorizationForm(driver) # Создаём объект перед вызовом метода
        my_ads_page = MyAdsPage(driver)


        # Открываем форму авторизации в хедере
        login_page.login_popup()

        # Вводим логин
        login_page.input_email()

        # Кликаем "Войти"
        login_page.sing_in()

        # Вводим пароль
        login_page.input_password_mail()

        # Кликаем "Войти"
        login_page.sing_in()

        # Проверяем авторизацию переходом в Мои объявления
        my_ads_page.open_profile()

        # Проверяем что авторизация есть
        ads_title = my_ads_page.get_title_myads()

        assert "Мои объявления" or "My Ads" in ads_title
