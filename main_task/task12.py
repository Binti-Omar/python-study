# Write a program that prints the largest of 4 inputs taken as input from a user.

no1=int(input('enter your number: '))
no2=int(input('enter your number: '))
no3=int(input('enter your number: '))
no4=int(input('enter your number: '))

if no1>no2 and no1>no3 and no1>no4:
    print('no1 is the largest')
elif  no2>no1 and no2>no3 and no2>no4:
    print('no2 is the largest')
elif no3>no1 and no3>no2 and no3>no4:
    print('no3 is the largest')
else:
    print('no4 is the largest')