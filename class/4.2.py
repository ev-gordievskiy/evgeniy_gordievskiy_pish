test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

len_test_list = len(test_list)

for i in range(len_test_list):
    if test_list[i] % 2 == 0:
        print(test_list[i], end=" ")

print()

for number in test_list:
    if number % 2 != 0:
        print(number, end=" ")

print()

test_list = [10, "Привет", 5.5, None]

print(test_list)

# Список с такими данными нельзя алгебраически преобразовывать

#for number in test_list:
#    if number * 2 == 0:
#        print(number, end=" ")
