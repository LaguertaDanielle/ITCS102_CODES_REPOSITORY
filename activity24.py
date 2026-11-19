#list & dictionaries

names = ["Jessica", "Diane", "Daniel", "Nicole", "Maria", "Angela", "Faith", "Josh", "Robin"]

#dictionary
#keys, value
names_d = {"Female1":"Jessica", "Female2":"Diane", "Male1":"Daniel", "Female3":"Nicole", "Female4":"Maria", "Female5":"Angela", "Female6":"Faith", "Male2":"Josh", "Male3":"Robin"}

print(names[8])

print(names_d["Female1"])

#traversing a dictionary

for x, y in names_d.items():
    print("key is ",x,"--> value is ", y)