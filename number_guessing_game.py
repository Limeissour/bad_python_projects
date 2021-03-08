import random
random_number = random.randint(0, 100)
print('There is a random number between 1 - 100')
nice = True
while nice:
    guess = int(input('Guess the number > '))
    if guess == random_number:
        print('WoW you won :D')
        break
    elif guess < random_number:
        print('Too low :(')
    elif guess > random_number:
        print('Too high :(')
