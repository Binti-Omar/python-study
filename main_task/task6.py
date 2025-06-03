# Write a program that lets the user input a password. 
# Give them only 4 attempts to check the passwords entered against “admin@123”.
# If the password is correct access is granted. After you show them a message , the account is blocked.

correct_password="admin@123"
attempts=4
for i in range(1,attempts+1):
    password=input("enter the password: ")
    if password==correct_password:
        print('access is granted')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'access denied,you have {remaining_attempts} left')
        else:
            print('the account is blocked')