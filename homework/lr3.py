import copy

print("Задание 1\n")


def sdvig (array, shift): 
    a = array.copy()    # Копируем исходный список
    k = len(a)          # Определяем длину списка
    if k < shift:       # Сравниваем длину списка с величиной сдвига
        print("Длина сдвига больше длины списка")
    else:
        return a[k-shift:] + a[:k-shift]    # Возвращаем список с измененым порядком членов

array = [1, 2, 3, 4, 5]
shift = 2

array_s = sdvig (array, shift)
print("Исходный список:", array,"\nСписок со сдвигом:", array_s)


print("\nЗадание 2\n")


def sdvig_matrix (matrix, shift): 
    a = matrix.copy()       # Копируем исходный список
    for i in range(len(a)): # Запускаем цикл с заменой списков внутри матрицы
        k = len(a[i])       # Определяем длину каждого списка в матрице
        b = a[i]            # Присваиваем переменной b значение списка
        b = b[k-shift:] + b[:k-shift]   # Меняем члены внутри списка
        a[i] = b            # Обратно присваиваем списку измененное значение

    return a                # Возвращаем матрицу со изменеными списками


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
shift = 1

matrix_s = sdvig_matrix (matrix, shift)
print("Исходная матрица:", matrix,"\nМатрица со сдвигом:", matrix_s)


print("\nЗадание 3\n")


def razv (array, blok_size): 
    a = array.copy()             # Копируем исходный список
    k = len(a) // block_size     # Определяем целое количество блоков
    for i in range(0, k) :       # Запускаем цикл по блокам
        b = (a[i*block_size:(i+1)*block_size])      # Внутри блока определяем список членов
        a[i*block_size:(i+1)*block_size] = b[::-1]  # Разворачикаем список внутри блока

    return a                    # Возвращаем список с измененным порядком членов


array = [1, 2, 3, 4, 5, 6, 7]
block_size = 3

array_s = razv (array, block_size)
print("Исходный список:", array,"\nСписок с разворотом поблочно:", array_s)


print("\nЗадание 4\n")


def podmassa (array, k): 
    a = array.copy()            # Копируем исходный список
    max_sum = 0
    for i in range(len(a)-k+1): # Запускаем цикл по списку
        b = (a[i:i+k])          # Внутри блока определяем список членов
        sum = 0
        for y in range(k):      # Запускаем цикл по блоку
            sum = sum + b[y]    # Суумируем члены внутри блока
        if max_sum < sum:       # Сравниваем полученную сумму с максимальной
            max_sum = sum
            max_str = b
           
    return max_str, max_sum     # Возвращаем список максимальной строкой и максимальной суммой


array = [1, -2, 3, 4, -1, 2, 1, -5, 4]
k = 3

array_s = podmassa (array, k)
print("Исходный список:", array,"\nСтрока с максимальной суммой k членов:", array_s[0],"\nМаксимальная сумма k членов:", array_s[1])