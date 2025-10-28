#test_tuple = (0, 1, 2 , 3 , 4, 5)

#for value in test_tuple:
#    print(value, end=" ")

test_tuple = (1, 2, 3)

len_test_tuple = len(test_tuple)
print(len_test_tuple)

x1, x2, x3 = test_tuple

print(x1, x2, x3)

student1 = ("Николай", 3, 22)
student2 = ("Дмитрий", 2, 21)

list_of_student = [student1, student2]

for name, grade, age in list_of_student:
    print(name, grade, age)
    

test_set = {1, 2, 3, 4, 5}

print(test_set)

test_list = [1, 1, 2, 2, 3, 3]

test_set_autoremove = list(set(test_list))
print(test_set_autoremove)

test_set1 = {1, 2, 3, 4, 5}
test_set2 = {6, 1, 2, 3, 7}

res = test_set1 ^ test_set2
print(res)