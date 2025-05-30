number=9
attempts=3

for i in range(1,attempts+1):
    guess=int(input("guess the number: "))
    if guess==number:
        print('you guessed it right')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f"you have{remaining_attempts} attempts left")
        else:
            print('you have run out of attempts')


