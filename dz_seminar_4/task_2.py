"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление."""

def create_dict(**kwargs):
    result_dict = {}
    for key, value in kwargs.items():
        key_str = str(key) if not isinstance(key, (int, float, complex)) else key
        result_dict[value] = key_str
    return result_dict


kwargs_dict = create_dict(name='Aleks', age=40, city='Moscow')
print(kwargs_dict)
