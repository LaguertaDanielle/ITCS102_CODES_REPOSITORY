#write a python program that accepts an integer number as age
#and determine the age group label base of that age input

name = input("Input Name: ")
age = int(input("Input Age: "))

print("Hi, ", name, ".That age is considered as ")
if age >= 1 and age < 5:
	print("Infant")

elif age >= 6 and age <= 12:
	print("Kid")

elif age >= 13 and age <= 19:
	print("Teenager")

elif age >=20 and age <= 29:
	print("Early Adulthood")

elif age >=30 and age <= 48:
	print("Adult")

elif age >=49 and age <= 59:
	print("Advance Adult")

elif age >=60 and age <= 150:
	print("Seinor")

else:
	print("Invalid")

