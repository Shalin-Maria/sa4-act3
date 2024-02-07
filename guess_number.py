number = 10
max_guesses = 5
for guess_count in range(max_guesses):
    print("I'm thinking of a number...")
    guess = int(input("What number am I thinking of? "))
    if guess == 'q':
        break
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    if guess_count == max_guesses - 1:
        print("Out of guesses! The secret number was:", number)
        break
if guess == 'q':
  print("The secret number was:", number)