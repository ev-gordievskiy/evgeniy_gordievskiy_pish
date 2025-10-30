print("Привет 'Очень большой' мир!")

string = """Можно
писать
целые абзацы
с
текстом и все
будет
хорошо!!"""

print(string)

str1 = "Привет"
str2 = " мир"
str3 = str1 + str2
print(str3)

integer_one = 1
prefix = "pref_"

full_string = prefix + str(integer_one)
print(full_string)

print ("    Привет\t\t\tМир\n".strip())

s = "Волков; Петров; Иванов; Сильм; Васечкин"
name_list = s.split("; ")
print(name_list)

s = "Волков Петров Иванов Сильм Васечкин"
name_list = s.split()
print(name_list)

s = "\n".join(name_list)
print(s)

email = "...@mail.ru"
name = "Иван Иванович"
phone_number ="8 999 999 99 99"

s = ";".join([name, email, phone_number])
print(s)

s = "I love Java"
s_new = s.replace("Java", "Python")
print(s_new)

print("b=1 c=2 d=3".replace("=", " "))

input_string = "b=1 c=2 d=3"
list_of_strings = input_string.split()
result_list = []
for string in list_of_strings:
    name, value = string.split("=")
    print(name, value)
    result_list.append((name, int(value)))
print(result_list)


