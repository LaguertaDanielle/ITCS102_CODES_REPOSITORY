age = int(input("What is your age: "))
isEmployed = bool(input("Are you currently employed? (True/False): "))
credit_score = int(input("Credit score: "))
annual_income = float(input("How much is your annual income? "))
has_collateral = bool(input("Do you have any collateral? (True/False): "))

base_rate = 0.0
if age >=21 and isEmployed == True:
    print("Accepted Baseline Criteria")
    if credit_score >= 750:
        print("You have a high credit score")
        if annual_income >= 1000000:
           base_rate = 4.5
        print("Your base rate is ", base_rate)
    else:
            base_rate = 5.0
            print("Your base rate is", base_rate)
     elif credit_score >= 600 and credit_score <750:
        print("Your credit score is less than 750")
        if has_collateral == True
        print("You have a collateral")
        base_rate = 7.0
        print("Your base rate is" , base_rate)
    
        