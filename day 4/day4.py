# Rock Paper Scissors
import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    
    choice = int(input("Make your choice: "))
    if choice== 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    elif choice == 3:
        choice_name = "Scissors"
    
    print(f"The user choice is: {choice_name} - {choice}")
    comp_choice = random.randint(1,3)
    if comp_choice== 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    elif comp_choice == 3:
        comp_choice_name = "Scissors"
        
    print(f"The computer choice is: {comp_choice_name} - {comp_choice}")
    
    if(choice == comp_choice):
        print("DRAW")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Computer won")
    elif(choice == 2 and comp_choice == 1) or (choice == 3 and comp_choice == 2) or (choice == 1 and comp_choice == 3):
        print("You won")