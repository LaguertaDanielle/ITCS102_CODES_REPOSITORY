fruits = ["apple", "star apple", "pineapple", "mango", "grapes", "orange", "duhat"]
print(fruits) #<-- this will print all the fruits mentioned

fruits.append("star apple") #<-- this will print specifically the said str/fruit
fruits.append("apple") #<-- this will print specifically the said str/fruit
print(fruits)
fruits.append("pineapple")
fruits.append("mango")
fruits.append("grapes")
print(fruits)

#index --> address, ZERO
print(fruits[0]) #<-- this will print the first str/fruit mentioned (apple)
print(fruits[3]) #<-- this will print the 4th str/fruit mentioned (mango)
print(fruits[0:3]) #<-- this will give range from the fruits mentioned (from apple to pineapple)
