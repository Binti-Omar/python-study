credits_score=int((input("Enter your credit score: ")))
if credits_score >700:
    annual_income = int(input("Enter your annual income: "))
    if annual_income > 50000:
        print("loan approved")
    else:
        print("income requirement not met")
else:
    print("credit score too low")