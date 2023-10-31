'''В большой текстовой строке text подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания, цифры и регистр символов.
Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после
того, как убрали знак препинания апостроф) считать двумя словами.
Цифры за слова не считаем.
Отсортируйте по убыванию значения количества повторяющихся слов.'''

text = "Python 3.9 is the latest version of Python. It's awesome!"
#text = "Python 3.9 is the latest version of Python. It's awesome!"
text = text.lower().replace('3', '').replace('9', '').replace('!', '').replace(
    '?', '').replace('.', '').replace(',', '').replace('  ', ' ').replace("'",
                                                                          ' ').split()
text = {i: text.count(i) for i in text}
print(sorted(text.items(), key=lambda x: x[1], reverse=True)[:10])