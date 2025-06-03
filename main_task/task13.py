# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” 
# and password is “Admin@123” , if so then print  “Login is Successful” and 
# if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.

correct_password='Admin@123'
correct_email='admin@gmail.com'
attempts=3
for i in range(1,attempts+1):
    email=input('enter your email: ')
    if email!=correct_email:
        remaining_attempts=attempts-i
        print(f'invalid username,you have {remaining_attempts} attempts left')
    else:
        print('valid email')
        password=input('enter your password: ')
        if password==correct_password:
            print('valid password')
        else:
            remaining_attempts=attempts-i
        print(f'invalid username,you have {remaining_attempts} attempts left')