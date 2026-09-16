#values
age = int(input("What is your age?: "))
isEmployed = bool(input("Are you currently employed? (True/False): "))
credit_score = int(input("Credit Score: "))
annual_income = float(input("What is your annual income? :"))
has_collateral = bool(input("Do you have any collateral? (True/False): "))

base_rate = 0.0
#base eligibility
if age >= 21 and isEmployed == True: #TIER 1
    print("Accepted Base Criteria")
    if credit_score >= 750:
        print("You have a high credit score. ")
        if annual_income >= 100000:
            base_rate = 4.5
            print("Your base rate is", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is", base_rate)
    elif credit_score >= 600 and credit_score < 750: #TIER 2
        print("Your base cost is lower than 750.")
        if has_collateral == True:
            print("You have a collateral. ")
            base_rate = 7.0
            print("Your base rate is", base_rate)
        elif annual_income <= 40000:
            print("Low annual income. ")
            base_rate = 9.5
            print("Your base rate is", base_rate)

        elif age >= 21 and isEmployed == True:
            if credit_score <= 600: #TIER 3
                print("Rejected: Credits score too low.")
        
else:
    print("Rejected: Fails Baseline Criteria")    