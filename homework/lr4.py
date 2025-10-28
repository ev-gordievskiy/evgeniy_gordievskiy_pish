print("Задание 1\n")

def creating_list(text):    # Функция преобразования строки с элементами, разделенными пробелами в список элементов
    text_list = []          # Создаем пустой список
    element = ""            # Создаем пустой элемент
    for i in range(len(text)):  # Запускаем цикл по символам исходной строки
        if text[i] != " ":      # Проверка на пробел
            element = element + text[i] # Добавление символа к элементу строки
        else:
            text_list.append(element)   # Добавление получившегося элемента в список  
            element = ""                # Обнуление элемента строки
    text_list.append(element)  # Добавление последнего элемента в список

    return text_list        


sentence = "apple banana apple orange banana kiwi"
list_sentence = creating_list(sentence) # Преобразование исходной строки в список элементов
list_sentence_original_sort = sorted(list(set(list_sentence)))  # Формирование списка оригинальных имен списка, упорядоченных по алфавиту
print("Исходный список:", sentence)
print("Отсортированный по алфавиту список оригинальных имен:", list_sentence_original_sort)


print("\nЗадание 2\n")


def create_dict_string(string):                  # Создаем фунцию формирования словаря из букв и их количества в строке
    list_string_sort = sorted(list(set(string))) # Формируем список ключей для словаря
    dict_string = {}    # Создаем пустой словарь
    sum_letters = 0     # Создаем счетчик букв     
    for i in range(len(list_string_sort)):  # Запускаем цикл по ключам из списка
        for y in range(len(string)):        # Запускаем цикл по буквам из строки
            if list_string_sort[i] == string[y]:    # Сравниваем ключ и букву
                sum_letters += 1                  
        dict_string[list_string_sort[i]] = sum_letters  # Добавляем ключу из списка значение счетчика букв
        sum_letters = 0

    return dict_string


string = "abracadabra"
dict_string = create_dict_string(string)

print("Исходная строка:", string)
print("Частота каждого символа в строке", dict_string)


print("\nЗадание 3\n")

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list_res = sorted(list(set(list1) & set(list2)))

print("Исходные списки:")
print(list1)
print(list2)
print("Элементы которые присутствуют в обоих списках", list_res)


print("\nЗадание 4\n")


n = 5
dict_sqrt = {}              # Создаем пустой словарь
for i in range(1, n+1):     # Запускаем цикл от 1 до n включительно
    dict_sqrt[i] = i ** 2   # Заполняем словарь ключами и значениями

print("Число n:", n)
print("Список чисел и их квадратов от 1 до n:\n", dict_sqrt)


print("\nЗадание 5\n")

    
string1 = "listen"
string2 = "silent"
dict_string1 = create_dict_string(string1) # Вызываем функцию формирования словаря из букв и их количества в строке (Задача 2)
dict_string2 = create_dict_string(string2)
check = dict_string1 == dict_string2

print("Исходные строки:", string1, string2)
print("Проверка строк на анаграмму:", check)    

