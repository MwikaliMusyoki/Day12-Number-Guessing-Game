import random
from art import logo
print(logo)


print("Ready to show off your guessing power? \n I'm thinking of a number between 1 and 100 🤔 ")

computer_number = random.randint(1, 101)
print(computer_number)

difficulty_level = input(
    "Choose a difficulty level to guess the number. 'easy' or 'hard' \n")


def play():
    game_on = True
    if difficulty_level == "easy":
        attempts = 10
    else:
        attempts = 5
    while game_on == True:
        print(f"You have {attempts} left to guess the number")
        user_guess = int(input("Make a guess :\n"))
        if user_guess > computer_number:
            print("Too high \n Guess again.")
        elif user_guess < computer_number:
            print("Too low \n Guess again.")
        elif user_guess == computer_number:
            print(f"You got it! The number is {computer_number}")
            game_on = False
        attempts -= 1


play()
