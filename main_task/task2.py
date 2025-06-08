# # TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# # Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display either “odd” or “even” to the user.
# #  Hint: how does an even / odd number react differently when divided by 2?
# # Extras:
# # If the number is a multiple of 4, print out “divisible by 4”.

# number=int(input('enter number: '))
# if number%2==0:
#     print('even')  
#     if number%4==0:
#         print('divisible by 4')
#     else:
#         print('not divisible by 4')
# else:
#     print('odd') 

def number(no):
    if no %2==0:
        result='even'
        if no%4==0:
            result= 'divisible  by 4'
        else:
            result=not 'divisible by 4'
    else:
        result='odd'
    print(f'the number is {result}')

numb=int(input('enter number:'))
number(numb)


