def my_factorial(n):
    fact = 1
    for x in range(n, 0, -1):
        fact * = x
    print(f"Factorial of {n} is {fact} ")

my_factorial(7)
my_factorial(4)
my_factorial(13)

#advantages
# * customization
# * code reusability