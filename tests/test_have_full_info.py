import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_have_full_info(show_my_pets):
    '''Проверяем, что у всех питомцев есть возраст, имя, порода'''
    # Получаем информацию обо всех питомцах
    pytest.driver.implicitly_wait(10)
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody tr')

    #Перебираем всю информацию,оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
   # с ожидаемым результатом
    for i in range(len(pets)):
        info_pets = pets[i].text.replace('\n', '').replace('×', '')
        split_info_pets = info_pets.split(' ')
        result = len(split_info_pets)
        assert result == 3