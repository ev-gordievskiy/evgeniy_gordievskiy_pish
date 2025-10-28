student1 = ("Николай", 3, 22)
student2 = ("Дмитрий", 2, 21)
student3 = ("Петр", 2, 21)

list_of_student = [student1, student2, student3]

for name, grade, age in list_of_student:
    if name == "Петр":
        print("Нашел Петра")


#           Ключ 1      Знач 1   Ключ 2     Знач 2
test_dict = {"Николай": (3, 22), "Петр": (2, 21)}

grade, age = test_dict["Николай"]
print(grade, age)

test_dict["Дмитрий"] = (4, 23)

del test_dict["Николай"]
print(test_dict)

for grade, age in test_dict.values():
    print(grade, age)

for name in test_dict.keys():
    print(name)
    
# дан список, множеством выбрать уникальные, потом отсортирвать по имени
# задача про словари, буквы
# взять два списка, преобразовать в множества, сделать пересечение, преобразовать в список, отсортировать в порядке возрастания
array = [1, 2, 5, 4]
print(sorted(array))
# использовать все типы коллекций