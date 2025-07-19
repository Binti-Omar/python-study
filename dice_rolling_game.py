attempts=4
random_number = 6  # Fixed number for the game
for i in range(1, attempts + 1):
    question = input('Do you want to play a dice rolling game? (yes/no): ').lower()
    if question=='yes':
        print('Welcome to the dice rolling game!')
        guess = int(input('Guess a number between 1 and 6: '))
        