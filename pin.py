pin='2013'
attempts=3
for i in range(1,attempts+1):
    guess=input("enter the pin: ")
    if pin==guess:
        print('correct pin')
        break
    else:
        remaining_attempts=attempts-i
        if pin!=guess:
         print(f"you have {remaining_attempts} attempts left")
        else:
            print('no more attempts')