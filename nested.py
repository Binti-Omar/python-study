# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low.
credits_score=int((input("Enter your credit score: ")))
if credits_score >700:
    annual_income = int(input("Enter your annual income: "))
    if annual_income > 50000:
        print("loan approved")
    else:
        print("income requirement not met")
else:
    print("credit score too low")


 # Write a Python program that checks if a variable student_score is greater than 90.
#  If true, check if the attendance is greater than 80.
#  If both conditions are true, print "Excellent student", 
# otherwise print "Good score, but attendance needs improvement"
student_score=96
attendance=79
if student_score > 90:
    if attendance >80:
      print("Excellent student")
    else:
      print("good score,but attendance needs improvement. ")
else:
   print("good score") 

   