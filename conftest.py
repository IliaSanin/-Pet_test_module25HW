import pytest
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(autouse=True)
def start_page():
   pytest.driver = webdriver.Chrome('C:\drivers\chromedriver.exe')
   pytest.driver.set_window_size(1400, 1000)

# Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

# Нажимаем на кнопку "Войти"
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# # кликнуть на пункт меню "Мои питомцы"
#    pytest.driver.find_element(By.XPATH, '//*[@href=\"/my_pets\"]').click()
