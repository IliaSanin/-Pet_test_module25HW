import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_all_my_pets(show_my_pets):
   '''Проверяем, что на странице пользователя присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')))

# Получаем кол-во всех питомцев
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')
   all_pets = len(pets)

# Получаем кол-во питомцев из информации пользователя, Выделяем из полученного списка число питомцев
   list_of_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
   num_pets = list_of_pets[0].text.split('\n')
   num_pets = num_pets[1].split(' ')
   num_pets = int(num_pets[1])

# Проверяем, что кол-во питомцев на странице соответствует кол-ву в информации пользователя
   assert all_pets == num_pets
