# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal.Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

email=(input("enter the email: "))
if email.find('@')==-1 and email.count('.')==-1:
    print('invalid email')
else:
    print('valid email')