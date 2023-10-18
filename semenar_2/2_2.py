data =[1, 1.3, 'abc', True, None, b'12']

for i, el in enumerate(data, 1):
    print(f'{i}. {el}, {el.__sizeof__()}, {hash(el)}')
    if type(el) == int and el > 0:
        print('целое число')
    elif type(el) == str:
        print('строка')