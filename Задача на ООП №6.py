"""Имеется пустой класс Config. Ваша задача написать функцию create_instance, которая принимает
на вход положительное число N. Функция должна создать ЭК , создать у него N атрибутов и вернуть
в качестве ответа полученный ЭК.
Что касается атрибутов, они должны называться определенным образом и иметь определенное значение.
В общем виде это можно записать так attribute<n> = "value<n>" где n — порядковый номер атрибута.
Значение атрибута - строковый тип. Если в функцию create_instance передали значение 3, то нужно
создать следующие атрибуты и значения:
# Если передать в функцию значение 3
obj = Config()
obj.attribute1 = "value1"
obj.attribute2 = "value2"
obj.attribute3 = "value3"
Ваша задача написать только определение функции create_instance, и не забывайте, что она должна вернуть ЭК."""
class Config:
    pass

def create_instance(n: int) -> Config:
    obj = Config()
    for i in range(1, n+1):
        setattr(obj, 'attribute' + str(i), 'value' + str(i))
    return obj

# Ниже расположены проверки для функции create_instance

config_2 = create_instance(2)
assert isinstance(config_2, Config)
assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}

config_3 = create_instance(3)
assert isinstance(config_3, Config)
assert config_3.__dict__ == {'attribute1': 'value1',
                             'attribute2': 'value2',
                             'attribute3': 'value3'}

print('good')