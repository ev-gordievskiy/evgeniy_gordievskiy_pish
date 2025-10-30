print("Задание 1\n")

data = "Иванов Иван, 20, Математика; Петров Петр, 21, Физика; Сидоров Сидор, 22, Химия"

print("Исходная строка:\n",data, "\n")
print("Форматированный вывод:\n")

student_list = data.split("; ")     # Создаем список студентов
for student in student_list:        # Запускаем цикл по списку студентов
    student = student.split(", ")   # Создаем список с данными студентов
    name, age, dep = student[0], student[1], student[2] # Раскладываем данные по переменным 
    res_string = f"Имя: {name}\nВозраст: {age}\nФакультет: {dep}\n" # Форматируем вывод
    print(res_string)


print("\nЗадание 2\n")


text = "Контакты: ivanov@example.com, petrov@work.net, sid@mail.ru"
email_list = (text.split(": ")[1]).split(", ")  # Первым сплитом делим строку на 2 части "Контакты" и адреса
                                                # Вторым сплитом формируем список адресов

print("Исходная строка:\n",text,"\n")
print("Список с адресами Электронной почты:\n", email_list)


print("\nЗадание 3\n")


sentence = "Python is a powerful and easy-to-learn programming language."
words = sentence.split()    # Делаем из строки список
sum_words = len(words)      # Определяем длину списка
print(f"""Предложение '{sentence}' 
содержит {sum_words} слов""")


print("\nЗадание 4\n")


s = "aaabbbcccaaadddd"
s_list = []                 # Создаем пустой список
for i in range(len(s)):     # Запускаем цикл по исходной строке
    if s[i] != s[i-1]:      # Сравниваем текущую букву с предыдущей
        s_list.append(s[i]) # Если не повторяется то записываем в список
print(f"""Исходная строка: '{s}'
Список символов по одному для каждого фрагмента: {s_list}""")


print("\nЗадание 5\n")


text = "Сегодня 20 градусов, завтра будет 18 градусов, а вчера было 22 градуса."

text_list = text.split()        # Разделяем текст на список 
numbers = text_list.copy()      # Копируем исходный список в тот, с которым будем работать
for word in text_list:          # Запускаем цикл по исходному списку
    try:
        number = int(word)      # Пробуем преобразовать в число
    except ValueError:
        numbers.remove(word)    # При наличии ошибки удаляем это слово из редактируемого списка   

print(f"""Исходная текст:
'{text}'
Только числа из этого текста: {numbers}""")
