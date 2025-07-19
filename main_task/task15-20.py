# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable

#a function to calculate the gross salary
def gross_salary (basic_salary,benefits):
     gross=basic_salary+benefits
     return gross
a=float(input('enter the salary: '))
b=float(input('enter the benefit: '))

grosssalary=gross_salary(a,b)
print(grosssalary)

def nhif(gross_salary):
    if gross_salary <=5999:
        nhif=150
    elif gross_salary >=6000 and gross_salary <= 79999:
        nhif=300
    elif gross_salary >=8000 and gross_salary <= 11999:
        nhif=400
    elif gross_salary >=12000 and gross_salary <= 14999:
        nhif=500
    elif gross_salary >=15000 and gross_salary <= 19999:
        nhif=600
    elif gross_salary >=20000 and gross_salary <= 24999:
        nhif=750
    elif gross_salary >=25000 and gross_salary <= 29999:
        nhif=850
    elif gross_salary >=30000 and gross_salary <= 34999:
        nhif=900
    elif gross_salary >=35000 and gross_salary <= 39999:
        nhif=950
    elif gross_salary >=40000 and gross_salary <= 44999:
        nhif=1000
    elif gross_salary >=45000 and gross_salary <= 49999:
        nhif=1100
    elif gross_salary >=50000 and gross_salary <= 59999:
        nhif=1200
    elif gross_salary >=60000 and gross_salary <= 69999:
        nhif=1300
    elif gross_salary >=70000 and gross_salary <= 79999:
        nhif=1400
    elif gross_salary >=80000 and gross_salary <= 89999:
        nhif=1500
    elif gross_salary >=90000 and gross_salary <= 99999:
        nhif=1600
    elif gross_salary >=100000 :
        nhif=1700
    return nhif
calculate_nhif=nhif(grosssalary)
print(calculate_nhif)

# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
# Write a normal program but use functions if you feel comfortable.
def nssf(gross_salary):
    calculated_nssf=6*gross_salary
    if gross_salary >=18000:
        value=calculated_nssf
    else:
        value='invalid'
        print(f'the nssf is {value}')
nssf(50000)

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
# Write a normal program but use functions if you feel comfortable.

# Task 18: Using Python or PHP or Java or Ruby or JavaScript
# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
# Write a normal program but use functions if you feel comfortable.

# TASK 19: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
# Write a normal program but use functions if you feel comfortable.

# Task 20: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

# Write a normal program but use functions if you feel comfortable.