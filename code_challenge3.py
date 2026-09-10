#Problem: Global Freight Calculator

#inputs

name = input("What is your name: ")
item = input("Type of Item: ")
isFragile = bool(input("Is the item fragile? (yes/no): ") == "yes")
isExpress = bool(input("Is it urgent? (yes/no): ") == "yes")
isInternational = bool(input("Is it international? (yes/no): ") == "yes")
weight = float(input("Weight in kilograms: "))
distance = float(input("Distance in kilometers: "))

#calculation of base cost

base_cost = (weight * 2.5) + (distance * 0.15)

if distance <= 100 and weight <= 2 and not isExpress and not isInternational:
	total = 0

elif isExpress and isInternational:
	total = (base_cost * 1.40) + 50

elif weight > 20 and isExpress or isInternational:
	total = (base_cost * 1.20) + 25

elif distance > 1000 or weight > 30:
	total = base_cost + 30

else:
	total = base_cost

shipping_fee = total - base_cost

#run
print("Name: ", name)
print("Type of Item: ", item)
print("Fragile: ", isFragile)
print("Express: ", isExpress)
print("International: ", isInternational)
print("Weight: ", weight)
print("Distance: ", distance)
print("Base Cost: PHP ", base_cost)
print("Shipping Fee: ", shipping_fee)
print("Expected Output:: PHP ", total)

