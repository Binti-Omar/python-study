# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable

basic_salary=float(input("enter your basic salary: "))
benefits=float(input('enter your benefits: '))
if basic_salary>=0 and benefits>=0:
    print('basic_salary,benefits')
else:
    print('basic_salary and benefits cannot be below zero')
gross_salary=basic_salary+benefits
print('gross_salary')
