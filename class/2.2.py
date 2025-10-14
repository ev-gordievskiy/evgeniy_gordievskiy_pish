for i in range(30,41):
    print(i ** 2)
    
# квадратные уравнения
import math
a = 3
b = 8
c = 5



def solve_qad_qe(a, b, c):
    D = b**2 - 4*a*c
    if D < 0:
        return None
    elif D == 0:
        print("Только один корень")
        x = (-b) / (2*a)
        return x, None
    else:
        print("Два корня")
        x1 = ((-b) + math.sqrt(D) / (2*a))
        x2 = ((-b) - math.sqrt(D) / (2*a))
        return x1, x2
    
x1, x2 = solve_qad_qe(a, b, c)


print(x1, x2)

print("Задание 1\n")


def func(x):
    if x >= (-2) and x <2:
        return x**2
    elif x >= 2:
        return x**2 + 4*x + 5
    else:
        return 4
    

x = 8

rez_prov = func(x)   
