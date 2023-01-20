import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_different_name(show_my_pets):
    '''Проверяем, что у всех питомцев уникальные имена'''
    # Получаем информацию обо всех именах питомцах
    pytest.driver.implicitly_wait(10)
    name = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')

    #Проверяем, что имена не повторяются
    assert len(set(name)) == len(name)
    print(f'Колличество уникальных имен: {len(set(name))}')
    print(f'Колличество имен: {len(name)}')

