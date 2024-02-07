number = 10
while True:
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
if guess == 'q':
  print("The secret number was:", number)