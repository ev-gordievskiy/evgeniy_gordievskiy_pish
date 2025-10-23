x = 5 // 2 #  деление без остатка
print(x)
y = (123 // 10) % 12
print(y)

x = 5
y = 5 

if x >= y:
    print("X больше или равно Y")
else:
    print("X не больше Y")
    
print(4 >> 1)

print(1 | 4)    
    
print(6 & 7)
    
print(~ (-6))

print(4 ^ 2)

x = 0
x = x | (1 << 0)
x = 0
x = x & ~(1 << 0)
a = 4
b = 2
z = (a ^ b) & 0
print(z)