file_name = "temperature_small.csv"
file = open(file_name, "r")
file.close()
 
with open(file_name, "r") as file:
    text = file.read()    
#print(text)
#print("\n")
with open(file_name, "r") as file:
    string = file.readline()  
#print(string)
#print("\n")
with open(file_name, "r") as file:
    strings = file.readlines()  
#print(strings)

with open(file_name, "r") as file:
    line = file.readline()

value_list = line.strip().split(";")
date = ":".join(value_list[:3])
time = ":".join(value_list[3:5])
temperature = int(value_list[5])


val_dict = {"Дата":date, "Время":time, "Температура":temperature}

with open("temperature_new.csv", "w") as f:
    f.write(";".join([str(val_dict["Температура"]), val_dict["Время"], (val_dict["Дата"])]))
    
with open("temperature_new.csv", "r") as file:
    line = file.readline()
    
print(line)