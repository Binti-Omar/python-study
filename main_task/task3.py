# TASK 3: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which gets a phone number from a form input or terminal.
#  Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1..
#  Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”

# phone_number=input('enter phone number: ')
# if phone_number.startswith('+254') and len(phone_number)==13:
#     valid=phone_number
# elif phone_number.startswith('07') and len(phone_number)==10:
#     valid="+254"+phone_number[1:]
# elif phone_number.startswith('7') and len(phone_number)==9:
#      valid="+254"+phone_number
# elif phone_number.startswith('254') and len(phone_number)==12:
#     valid='+'+phone_number
# elif phone_number.startswith('01')and len(phone_number)==10:
#     valid='+254'+phone_number[1:]
# elif phone_number.startswith('1') and len(phone_number)==9:
#     valid='+254'+phone_number
# else:
#     valid='invalid'
# print(f'{valid} is valid phone number')

def phone_number(no):
    if no.startswith('+254') and len(no)==13:
        valid=no
    elif no.startswith('07') and len(no)==10:
        valid="+254"+no[1:]
    elif no.startswith('7') and len(no)==9:
        valid="+254"+no
    elif no.startswith('254') and len(no)==12:
        valid='+'+no
    elif no.startswith('01')and len(no)==10:
        valid='+254'+no[1:]
    elif no.startswith('1') and len(no)==9:
        valid='+254'+no
    else:
        valid='invalid'
    print(f'{valid} is valid phone number')
number=input('enter phone number: ')
phone_number(number)


