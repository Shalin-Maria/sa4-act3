number = 10
while True:
    print("I'm thinking of a number...")
    guess = int(input("What number am I thinking of? "))
    if guess == 'q':
        break
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry! The number was {number}.")
if guess == 'q':
  print("The secret number was:", secret_number)