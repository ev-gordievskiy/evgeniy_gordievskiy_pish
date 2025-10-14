# Задача про героя

# У героя есть:

mech = 1
nozh = 2
yad = 1

# Условия старейшины

if mech >= 2 or yad >= 1 and nozh >= 2: # Проверка условий
    print("Geroy = True")
else:
    print("Geroy = Dragon win")


print("\nЗадание 1\n")


def func(x):
    if x >= (-2) and x <2: # Проверка условий
        return x**2
    elif x >= 2:
        return x**2 + 4*x + 5
    else:
        return 4
    

x = -0.25

rez_prov = func(x)   
print(rez_prov)


print("\nЗадание 2\n")


def nod(del_, ost):
    while ost != 0: # Запуск цикла, пока остаток не будет равен 0
        del_, ost = ost, (divmod(del_, ost)[1]) # Присвоение переменным делителя и остатка результата нового деления - остатка и делителя 
    return del_


a = 11439
b = 9225

nod_ = nod(a, b)
print(nod_)   


print("\nЗадание 3\n")


def sum_product(a):
    b = [int(c) for c in str(a)]   # Представление числа в виде строки с набором цифр        
    proverka = False
    sum = 0
    product = 1
    for i in range(len(b)): # Присвоение индексов каждой цифре в наборе
        sum = sum + b[i] # Результат суммы цифр числа
        product = product * b[i] # Результат произведения цифр числа
    if sum  == product: # Сравнение суммы и произведения
        proverka = True
    return proverka        


a = 132    
                
proverka_ = sum_product(a)
if proverka_:
    print("Сумма цифр числа", a, "равна их произведению") 
else:
    print("Сумма цифр числа", a, "не равна их произведению")


print("\nЗадание 4\n")


def sum_(a):
    b = [int(c) for c in str(a)]   # Представление числа в виде строки с набором цифр   
    sum = 0     
    for i in range(len(b)): # Присвоение индексов каждой цифре в наборе
        sum = sum + b[i] # Результат суммы цифр числа
    return sum    
    
                
a = 138

sum_c = sum_(a)
print(sum_c) 
