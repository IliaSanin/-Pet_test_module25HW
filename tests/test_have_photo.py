import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_have_photo(show_my_pets):
    '''Проверяем,что хотя бы у половины питомцев есть фото'''

    # Получаем кол-во всех питомцев и их фото
    pytest.driver.implicitly_wait(10)
    pets_photo = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody img')

    # Получаем кол-во питомцев из информации пользователя, Выделяем из полученного списка число питомцев
    list_of_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    num_pets = list_of_pets[0].text.split('\n')
    num_pets = num_pets[1].split(' ')
    num_pets = int(num_pets[1])

    #Ищем питомцев без фото
    half_pets = num_pets // 2
    count = 0
    for i in range(len(pets_photo)):
        if pets_photo[i].get_attribute('src') != '':
            count += 1

    # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
    assert len(pets_photo) >= half_pets
