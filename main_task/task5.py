# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max () function!

numb1=int(input('enter the first  number: '))
numb2=int(input('enter the second number: '))
numb3=int(input('enter the third number: '))

if numb1>numb2 and numb1>numb3:
    print('numb1 is the largest')
elif  numb2>numb1 and numb2>numb3:
    print('numb2 is the largest')
else:
    print('numb3 is the largest')
