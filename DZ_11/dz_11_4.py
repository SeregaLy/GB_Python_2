'''Задача о матричных операциях

Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые
операции с матрицами.
Атрибуты класса:
rows (int): Количество строк в матрице.
cols (int): Количество столбцов в матрице.
data (list): Двумерный список, содержащий элементы матрицы.
Методы класса:
__init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты
 rows и cols, а также создает двумерный список data размером rows x cols и
 заполняет его нулями.
__str__(self): Метод, возвращающий строковое представление матрицы.
Возвращаемая строка представляет матрицу, где элементы разделены пробелами, а
строки разделены символами новой строки. Например:
1 2 3
4 5 6
__repr__(self): Метод, возвращающий строковое представление объекта, которое
может быть использовано для создания нового объекта того же класса с такими же
размерами и данными.
__eq__(self, other): Метод, определяющий операцию "равно" для двух матриц.
Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество
строк и столбцов, а также все элементы равны. Иначе возвращает False.
__add__(self, other): Метод, определяющий операцию сложения двух матриц.
Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и
столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент
равен сумме соответствующих элементов входных матриц.
__mul__(self, other): Метод, определяющий операцию умножения двух матриц.
Проверяет, что количество столбцов в первой матрице равно количеству строк во
второй матрице. Если условие выполняется, создает новую матрицу, где элемент на
 позиции [i][j] равен сумме произведений элементов соответствующей строки из
 первой матрицы и столбца из второй матрицы.

'''


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols}, {self.data})"

    def __add__(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.data = [
                [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
                for i in range(self.rows)]
            return result
        else:
            raise ValueError("Матрицы разных размеров нельзя сложить!")

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Нельзя умножить матрицы с данными размерами!")
        result = Matrix(self.rows, other.cols)
        result.data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
             for j in range(other.cols)] for i in range(self.rows)]
        return result

matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 2)
matrix4.data = [[7, 8], [9, 10]]

result = matrix3 * matrix4
print(result)
