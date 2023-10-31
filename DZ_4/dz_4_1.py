'''
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в
аргументы matrix, и возвращает транспонированную матрицу.
'''

'''matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]'''


def transpose(matrix):
    transposed_matrix = [[0 for _ in range(len(matrix))] for _ in
                         range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


'''transposed_matrix = transpose(matrix)'''
