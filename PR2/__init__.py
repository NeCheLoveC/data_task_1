# %%
# 1.1 Извлеките все элементы массива с нечетными значениями из arr
import numpy as np

def a(arr):
    result = list()
    for i in arr:
        if (i % 2) == 1:
            result.append(i)
    return result
mas = np.array(range(10))
print(a(mas).__str__())

# %%
# 1.2 Замените все элементы массива с нечетными значениями на -1.
import numpy as np
mas = np.array(range(10))
mas[mas % 2 == 0] = -1
print(mas.__str__())

# %%
# 1.3	Преобразуйте массив в двухмерный массив (размерность 5х2).
import numpy as np
mas = np.array(range(10))
new_arr = mas.reshape((5,2))
print(new_arr.__str__())

# %%
# 1.4 Получите все элементы массива с номерами от 5 до 10.
import numpy as np
mas = np.array(range(10))
new_arr = mas[5:10]
print(new_arr.__str__())


# %%
# 2.1 Склеить массивы a и b, таким образом, что бы в итоге получить матрицу размерностью 5х4. Например:

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')

print(np.concatenate((a,b)).reshape((5,4)))


# %%
# 2.2 Склеить массивы a и b, таким образом, что бы в итоге получить матрицу размерностью 10х2. Например:

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')

print(np.concatenate((a,b)).reshape((10,2)))

# %%
# 2.3 Вывести на экран массив, который состоит из общих элементов массивов a и b

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')

print(np.intersect1d(a,b))

# %%
# 2.4 В массиве a удалить все элементы, которые содержатся в массиве b.

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')
print(np.delete(a, np.isin(a, b)))

# %%
# 2.5	Вывести на экран номера элементов, в которых значения элементов массивов a и b совпадают.

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')
print(np.where(np.isin(a, b))[0])

# %%
# 2.6 Вывести на экран все элементы от 3 до 7 в массиве a

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')

print(np.where(np.isin(a,range(3,8)))[0])

# %%
# 2.7 Умножить элементы массива b на 2. После этого перемножить элементы массивов a и b

import numpy as np
a = np.array(range(10), dtype='int64')
b = np.ones(10, dtype='int64')

b = b * 2
arr = a * b
print(arr)
