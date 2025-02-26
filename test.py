import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Запускаем браузер
driver = webdriver.Chrome()  # Убедись, что путь к WebDriver указан верно
driver.get("https://dev.bazaarorigin.com/")  # Открываем страницу
driver.maximize_window()
time.sleep(5)

# Кликаем по афише
driver.find_element(By.CSS_SELECTOR,'[data-testid="search_field"]').send_keys("вилла")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'[data-testid="search_button"]').click()
time.sleep(5)


