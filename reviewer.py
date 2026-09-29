age = int(input("What is your age: "))
monthly_rev = float(input("Your monthly revenue: "))
credit_score = int(input("Your credit score: "))
yrs_in_business = float(input("YEars in business: "))
has_defaults = bool(input("Has defaults?:"))
collateral_name = str(input("Collateral name: "))
collateral_value = float(input("Collateral value: "))

#eligibility check

max_loan = 0
base_fee = 0 
#tier 1
if age >= 21 and has_defaults == False and yrs_in_business >= 2.0 :
    print("Baseline Accepted")
    if credit_score >= 720:
        max_loan = 3 * monthly_rev
        if monthly_rev >= 50000:
            base_fee = max_loan * 0.015
        else:
            base_fee = max_loan * 0.025
            print("Monthly Revenue below 50000")
        #collateral
        if collateral_value >= max_loan:
            print("Collateral", collateral_value, "with a value of", collateral_value, "is accepted")
        else:
            print("Rejected: Insifficient collateral value for", collateral_value)
        #surcharge
        if collateral_value % 5000 != 0:
            base_fee += 250
            print("Additional base charge added to base fee, total base fee is", base_fee)
        else:
            print("Collateral value divisible by 5000")
#tier 2
    elif credit_score >= 620 and credit_score < 720 :
        max_loan = monthly_rev * 1.5
        if yrs_in_business >= 5.0 :
            base_fee = max_loan * 0.02
        else:
            base_fee = max_loan * 0.035
            print("Rejected: YEars in business is lower than 2.0")
         #collateral
        if collateral_value >= max_loan:
            print("Collateral", collateral_value, "with a value of", collateral_value, "is accepted")
        else:
            print("Rejected: Insifficient collateral value for", collateral_value)
         #surcharge
        if collateral_value % 5000 != 0:
            base_fee += 250
            print("Additional base charge added to base fee, total base fee is", base_fee)
        else:
            print("Collateral value divisible by 5000")
#tier 3
    elif credit_score < 620:
        print("Rejected: Credit score below requirement")

else:
    print("baseline Rejected")    