import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_different_pets(show_my_pets):
    '''Проверяем, что в списке нет повторяющихся питомцев'''
    # Получаем информацию обо всех питомцах
    pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Перебираем данные из pet_info, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_info = []
    for i in range(len(pet_info)):
        data_pet = pet_info[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_info.append(split_data_pet)

    # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_info:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')

    # Превращаем список в множество
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b

    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert result == 0

