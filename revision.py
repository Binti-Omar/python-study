# # Create a program that generates a random number,and the user has to guess the number.

# number=10
# guess=int(input('guess the number: '))
# if guess==number:
#     print('you guessed the number correctly')
# else:
#     print('you guessed the number incorrectly')

# number=10
# guess=int(input('guess the number: '))
# if guess==number:
#     valid='you guessed the number correctly'
# else:
#     valid='sorry,you guessed the number incorrectly'
# print(valid)

#LOOPS
number=10
attempts=3
for i in range(1, attempts + 1):
    guess=int(input('guess the number: '))
    if guess==number:
        print('congratulations! you guessed the number correctly')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'incorrect you have {remaining_attempts} attempts left')
        else:
            print('incorrect you have no attempts left')
            break

        