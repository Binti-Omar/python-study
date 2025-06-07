# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable

# basic_salary=float(input("enter your basic salary: "))
# benefits=float(input('enter your benefits: '))
# if basic_salary>=0 and benefits>=0:
#     print('basic_salary,benefits')
# else:
#     print('basic_salary and benefits cannot be below zero')
# gross_salary=basic_salary+benefits
# print('gross_salary')

# Employee's Monthly Gross Salary(Kshs) 	Monthly NHIF Contribution (Kshs)
# 5,999 	150
# 6,000 - 7,999 	300
# 8,000 - 11,999 	400
# 12,000 - 14,999 	500
# 15,000 - 19,999 	600
# 20,000 - 24,999 	750
# 25,000 - 29,999 	850
# 30,000 - 34,999 	900
# 35,000 - 39,999 	950
# 40,000 - 44,999 	1,000
# 45,000 - 49,999 	1,100
# 50,000 - 59,999 	1,200
# 60,000 - 69,999 	1,300
# 70,000 - 79,999 	1,400
# 80,000 - 89,999 	1,500
# 90,000 - 99,999 	1,600
# 100,000 and above 	1,700
# a function to calculate the gross salary
def gross_salary (basic_salary,benefits):
    gross=basic_salary+benefits
    print(f'the gross_salary is {gross}')
a=float(input('enter the salary: '))
b=float(input('enter the benefit: '))
gross_salary(a,b)

if gross_salary >=5999:
    nhif=150
elif gross_salary >=6000 and =< 7999:
