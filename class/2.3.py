import math
a = 3
b = 8
c = 5

D = b**2 - 4*a*c

x = D > 0

rain = True
fog = False

if rain and not fog:
    print("Беру зонт")
elif fog and rain:
    print("Беру дождевик")
    
x = True
y = False
z = x or y
print(z)
z = x and y
print(z)
z = not(x and y) or (y or not x)
print(z)

i = 10
i +=6
i -=4
print(i)


a = 5
b = 10
c = 14
g = 20

math_middle = (a + b) / 4
print(math_middle)


def middle_4(a, b, c, d):
    res = (a + b + c + d) / 4
    res += 10
    return res
middle_res = middle_4(a, b, c, g)
print(middle_res)

middle_res = middle_4(a + 20, b-2, c*2, g)
print(middle_res)