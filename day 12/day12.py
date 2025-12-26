# Number Guessing Project
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    is_difficulty = False
    while not is_difficulty:
        difficulty = input("Choose a difficulty, type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            is_difficulty = True
            return EASY_LEVEL_TURNS       
        elif difficulty == "hard":
            is_difficulty = True
            return HARD_LEVEL_TURNS
        else:
            print("Kindly choose the correct difficulty level...")


def check_answer(user_guess, actual_guess):
    if user_guess > actual_guess:
        print("HIGH")
    elif user_guess < actual_guess:
        print("LOW")
    else:
        print("You have choose the correct number")

def game():
    print("Welcome to the Number Guessing Game\n")
    print("I'm thinking of a number between 1 and 100")

    choose = randint(1,100)
    print(choose)
    attempts = set_difficulty()
    print(f"You have {attempts} attempts remaining to guess the number")
    is_correct = False

    while not is_correct:
        if attempts == 0:
            print("You lost, you have no attempts remaining!!!")
            is_correct = True
        else:
            guess = int(input("make a guess: "))
            check_answer(guess, choose)
            if guess == choose:
                is_correct = True
            elif guess != choose:
                attempts -= 1
                print(f"You have {attempts} remaining to guess the number")
        
game()