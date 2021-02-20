from random import randint
while True:
    print('There is a random number between 1 - 100')
    random_number = randint(0, 100)
    guess = int(input('Guess the number > '))
    if guess == random_number:
        print('WoW you won :D')
        break
    elif guess < random_number:
        print('Too low :(')
    else:
        print('Too high :(')
