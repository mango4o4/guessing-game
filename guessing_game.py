import random
secret_number = random.randint(1,100)
print('A random number between 1 and 100 (inclusive) has been generated.')


guesses_choice = input('Decide how many guesses you would like to have: ')
num_guesses = int(guesses_choice)

while num_guesses > 0:
    guess = input('Enter your guess: ')
    num_guesses = num_guesses - 1
    if int(guess) > secret_number:
        print("Guess lower")
        print("Attempts left:", num_guesses)
    if int(guess) < secret_number:
        print("Guess higher")
        print("Attempts left:", num_guesses)
    if int(guess) == secret_number:
        print('You won!')
        break
    if num_guesses == 0:
        print("You lost :(")
        break