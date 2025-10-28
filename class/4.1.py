x = 10
string = "str"
y = 5.5

#  Имя  Курс Ср. Балл

st1_name = "Николай"

# Множество имен
# Список
#        -3      -2           -1
#        0        1            2    
names = ["Юрий", "Николай", "Петр"]

grade = [2, 3, 5]

middle_score = [4.5, 2.3, 5.0]

print(names)

print(grade)

print(middle_score)

x1 = 20
x2 = 30

array = [x1, x2]

print(array)

name = names[1]

print(name)

# Пустой

test_list = []

for i in range(100):
    test_list.append(i)

# Заполнен на 100 значений
    


len_test_list = len(test_list)

for i in range(len_test_list):
    test_list[i] = i ** 2
    #print(test_list[i], end=" ")

#print(test_list)

last_item = test_list.pop()
print(last_item)
print()
print(test_list, len(test_list))