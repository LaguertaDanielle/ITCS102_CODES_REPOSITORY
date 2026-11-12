loan_amt = float(input("enter amount: "))
years = int(input("enter years to pay: "))
month = years * 12
principal = loan_amt / month
remaining_bal = loan_amt

for x in range(1, month+1):
    remaining_bal -= principal
    loan_int = remaining_bal * 0.00256
    monthly_pay = loan_int + principal
    #print(x, principal) or
    #print(x, round(monthly_pay), round(loan_int), round(principal,2), round(remaining_bal,2))

    #string formatting
    print(f"|{x} \+ | {round(monthly_pay,2)} \+ | \+ {round(loan_int,2)} \+ | \+ {round(principal,2)} \+ | \+ {round(remaining_bal,2)}")
