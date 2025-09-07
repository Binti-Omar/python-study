# def areatriangle():
def areatriangle(height,base):
    area=height*base*0.5
    print(area)
# areatriangle()
areatriangle(30,20)
areatriangle(50,40)


# create a function that checks if a number is an even or odd number

# def check_number():
def check_number(x):
    if x%2==0:
        print('the number is even')
    else:
        print('the number is odd')
# check_number()
check_number(26)
check_number(7)

# create a function to calculate area of a rectangle
def arearectangle(length,width):
    area=length*width
    print(area)
arearectangle(20,25)

# create a function that displays the largest number amongst the three numbers
# def number(no1,no2,no3):
#     if no1>no2 and no1>no3:
#         result=no1
#     elif no2>no1 and no2>no3:
#         result=no2
#     else:
#         result=no3
#     print(f' the largest number is {result}')
# number(30,90,76)

# how to use input
def number(no1,no2,no3):
    if no1>no2 and no1>no3:
        result=no1
    elif no2>no1 and no2>no3:
        result=no2
    else:
        result=no3
    print(f' the largest number is {result}')
first=int(input('enter the first number: '))
second=int(input('enter the first number: '))
third=int(input('enter the first number: '))
number(first,second,third)