'''
Напишите функцию key_params, принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ - значение переданного аргумента, а значение -
имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def key_params(**kwargs):  # kwargs - словарь
    return {v if v.__hash__ is not None and v != None else str(v): k for k, v
            in
            kwargs.items()}


params = key_params(a=None, b='hello', c=[1, 2, 3], d=None)
print(params)
