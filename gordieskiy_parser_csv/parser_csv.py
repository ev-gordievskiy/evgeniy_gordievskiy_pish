import optparse

def check_value(value, v_min, v_max):   
    # Функция проверки корректности значений исходного файла
    try:
        value = int(value)              # Преобразование значения в int
        if v_min <= value and value <= v_max:   # Сравнение с заданными пределами
            check_value = True
        else:
            check_value = False           
    except ValueError:          
        check_value = False             # Ошибка в случае несоответствия типу данных
    return check_value, value           # Возвращает результат проверки и значение, преобразованое в int

def stat(temp_list):
    # Функция подсчета статистики по списку               
    if not temp_list:
        return None, None, None             # Вывод в случае отсутствия данных
    t_av = sum(temp_list)/len(temp_list)    # Вычисление среднего
    t_max = max(temp_list)                  # Вычисление максимального
    t_min = min(temp_list)                  # Вычисление минимального
    return t_av, t_max, t_min

def main():
    # Создание парсера аргументов
    parser = optparse.OptionParser(usage="%prog [options]", 
                                   description="Анализ данных от датчика температуры из CSV файла")

    # Добавляем опции 
    parser.add_option("-f", "--file", dest="filename", 
                      help="входной файл CSV для обработки")
    parser.add_option("-m", "--month", dest="month", type="int",
                      help="вывести статистику только за указанный месяц (1-12)")
    
    # Парсим аргументы
    (options, args) = parser.parse_args()
    
    # Проверяем обязательные параметры
    if not options.filename:
        parser.print_help()
        return
    
    # Используем переданный файл
    file_name = options.filename
    
    try:
        with open(file_name, "r") as file:          # Открываем файл в режиме чтения
            strings_original = file.readlines()     # Передаем в список содержимое файла построчно    
    except FileNotFoundError:                       # Обработка ошибок
        print(f"Ошибка: Файл {file_name} не найден")
        return
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return
    
    strings = strings_original.copy()               # Копируем полученный список в переменную для последующей обработки

    # Создание кортежей с ключами столбцов исходного файла, списком месяцев и параметрами проверки исходных значений 
    keys = ("Год", "Месяц", "День", "Часы", "Минуты","Температура")
    mons_key = ("январь", "февраль", "март", "апрель","май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь","декабрь")
    parameters = ((2021, 2021), (1, 12), (1,31), (0, 23), (0, 59), (-99, 99))
    
    n_str = 0
    n_bug = 0
        
    for string in strings_original:                 # Запускаем цикл по строкам оригинального списка
    
        value_list = string.strip().split(";")      # Формируем список с исходными данными, почищенный от лишних символов

        date = ".".join(value_list[:3])             # Формируем строку "Дата"
        time = ":".join(value_list[3:5])            # Формируем строку "Время"
        check_list = []                             # Создаем пустой список ошибок
        
        for i in range(len(value_list)):            # Запускаем цикл по строке
            v_min, v_max = parameters[i]            # Считываем граничные условия для данного значения строки
            value = check_value(value_list[i], v_min, v_max) # Передаем значение на проверку
            check_list.append(value[0])             # Добавляем результат проверки в список ошибок
            if value[0] == False:                   # Если есть ошибка, выводим её параметры
                print(f"\nОшибка данных на {n_str} строке исходного файла. В столбце '{keys[i]}' значение '{value[1]}'")
                print(f"Дата и время ошибки: {date} {time}")
                n_bug += 1                          # Увеличиваем счетчик ошибок    

        check = list(set(check_list))[0]            # Проверка, что в проверяемой строке есть хотя бы одна ошибка
        if check == False:
            strings.remove(string)                  # Удаляем строку с ошибкой из списка значений для последующей обработки

        n_str += 1                                  # Увеличиваем счетчик строк   

    # Задаемся начальными условиями для дальнейшей обработки
    n_mon = 1
    temp_list_mon = []
    mon_value_dict = {}   
            
    for string in strings:                      # Запускаем цикл по строками списка с валидными значениями
    
        value_list = string.strip().split(";")  
        mon = int(value_list[1])                # Определяем значение месяца
        temp = int(value_list[5])               # Определяем значение температуры
        if mon > n_mon:                         # Проверяем, не изменился ли месяц
            mon_value_dict[mons_key[n_mon-1]] = temp_list_mon   # Если изменился, добавляем "пару месяц: список температур" в словарь
            temp_list_mon = [temp] 
        else:
            temp_list_mon.append(temp)          # Добавляем значение температуры в список текущего месяцв
        n_mon = mon
        
    mon_value_dict[mons_key[n_mon-1]] = temp_list_mon # Добавляем в словарь значения последнего месяца

    print(f"\nЧисло ошибок: {n_bug}. Статистика без учета строк с некорректными данными: \n") # Вывод количества обнаруженных ошибок

    # Обработка ключа -m, если указан конкретный месяц
    if options.month:
        if 1 <= options.month <= 12:                        # Проверка данных ключа на соответствие условиям
            month_name = mons_key[options.month - 1]        # Определяем имя месяца
            temp_list = mon_value_dict.get(month_name, [])  # Запрашиваем в словаре список температуры по этому месяцу
            
            if temp_list:   # Проверка списка на наличие данных
                mon_stat = stat(temp_list) # Запрос статистики по списку за месяц
                
                # Форматирование вывода статистики за искомый месяц                 
                print(f"Статистика за {month_name}:")
                print(f"Средняя температура: {mon_stat[0]}")
                print(f"Максимальная температура: {mon_stat[1]}")
                print(f"Минимальная температура: {mon_stat[2]}")
            else:
                print(f"Нет данных за {month_name}")
        else:
            print("Ошибка: номер месяца должен быть от 1 до 12")
    else:
        # Если месяц не указан, выводим статистику по всем месяцам
        for mon_name, temp_list in mon_value_dict.items(): # Запускаем цикл по словарю и разбираем его на ключ и список значений
            
            mon_stat = stat(temp_list) # Запрос статистики по списку за месяц
            
            # Форматирование вывода статистики за месяц   
            print(f"Статистика за {mon_name}")
            print(f"Средняя температура: {mon_stat[0]}")
            print(f"Максимальная температура: {mon_stat[1]}")
            print(f"Минимальная температура: {mon_stat[2]}")
            print()  
                
        temp_list_year = sum(mon_value_dict.values(), []) # Ормирование списка температур за год
        year_stat = stat(temp_list_year) # Запрос статистики по списку за год
            
        # Форматирование вывода статистики за год    
        print("_" * 60)
        print("ИТОГ")
        print(f"Средняя температура за год: {year_stat[0]}")
        print(f"Максимальная температура за год: {year_stat[1]}")
        print(f"Минимальная температура за год: {year_stat[2]}")

main()