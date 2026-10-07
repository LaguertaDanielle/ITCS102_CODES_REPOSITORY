name = str(input("Customer's name:"))
consumption = float(input("Water consumption in meter cube:"))

base_line = 10
bill = 150


if consumption <= 10:
    bill = 150
    print("Your water bill is", bill)
    if bill <= 500:
        print("Category: Regular Water")
        if bill >= 501 and bill <= 800:
            print("High water use")
            if bill >= 800:
                print("very high water use")
elif consumption >= 11 and consumption <= 20:
    bill = 150 + (consumption - 10) * 20
    print("Your total bill is", bill )
    if bill <= 500:
        print("Category: Regular Water")
        if bill >= 501 and bill <= 800:
            print("High water use")
            if bill >= 800:
                print("very high water use")

elif consumption >= 21 and consumption <= 30:
    bill = 150 + (10 * 20) + (consumption - 20) * 25
    print("Your total bill is", bill)
    if bill <= 500:
        print("Category: Regular Water")
        if bill >= 501 and bill <= 800:
            print("Category: High water use")
            if bill >= 800:
                print("Category: very high water use")

else:
    if consumption >= 30:
        bill = 150 + (10 * 20) + (10 * 25) + (consumption - 30) * 30
        print("Your total bill is", bill)
    print("over ka sa water consumption bes")
    if bill <= 500:
        print("Category: Regular Water")
        if bill >= 501 and bill <= 800:
            print("High water use")
            if bill >= 800:
                print("very high water use")
