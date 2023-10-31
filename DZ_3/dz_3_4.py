'''Дан список повторяющихся элементов lst. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.'''

lst = [1, 2, 3, 2, 4, 5, 4]


def find_duplicates(lst):
    duplicates = []
    count = {}
    for item in lst:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item, freq in count.items():
        if freq > 1:
            duplicates.append(item)
    return duplicates


result = find_duplicates(lst)
print(result)

