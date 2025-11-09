import random

print("Welcome to the number guessing game!")


while True:
    correct_number = random.randint(1, 100)
    guess_counter = 0

    print("I am thinking of a number between 1 and 100. Can you guess what it is?")
    while True:
        try:
            user_guess = int(input("Take a guess: "))
            guess_counter += 1

            if user_guess > correct_number:
                print("Your guess was too high, please try again. \n")
            elif user_guess < correct_number:
                print("Your guess was too low, please try again. \n")
            else:
                print(
                    f"Your guess was correct! It took you {guess_counter} tries.")
                break

        except ValueError:
            print("Please use a valid number and guess again. \n")

    play_again = input("Would you like to play again? (y/n); ").lower()
    if play_again == "y":
        print("Starting new game....")
    else:
        print("Thanks for playing! Goodbye.")
        break
