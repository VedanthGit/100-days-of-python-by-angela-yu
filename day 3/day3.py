# Pizza Order
print("Welcome to Pizza Home\n")
print("What would you like to have\n")
S = 15
M = 20
L = 25
print("Small[S]: 15$ | Medium[M]: 20$ | Large[L]: 25$")
size = input("What size of pizza would you like to have: ")
pepperoni = input("Would You like to have pepperoni? S: 2$ | M or L: 3$ | Y or N: ")
extra_cheese = input("Would You like to have extra cheese:1$? Y or N: ")

bill = 0
if size == 'S':
    bill += S
elif size == 'M':
    bill += M
elif size == 'L':
    bill += L
else:
    print("Kindly choose a valid option")

if pepperoni == 'Y' or pepperoni == 'Yes':
    if size == 'S':
        bill += 2
    elif size == 'M' or size == 'L':
        bill += 3
else:
    bill = bill

if extra_cheese == 'Y' or extra_cheese == 'Yes':
    bill += 1
    
print(F"Your Total Bill is: ${bill}")


# Treasure Hunt
# print("Welcome to the Treasure Island\n")
# print("There is an endless route which is an game over, Choose wisely\n")
# step1 = input("Left or Right: ")
# if(step1 == "Right" or step1 == "right"):
#     print("You entered an endless route, GAME OVER")
# else:
#     print("Congratulations, you can move to the next step")


# step2 = input("Choose an option wisely Swim or Walk: ")
# if(step2 == "Swim" or step2 == "swim"):
#     print("You got eaten by the crocodiles, GAME OVER")
# else :
#     print("Congratulations, you can move forward")

# step3 = input("Choose a door to enter -> Red or Blue or Yellow: ")
# if(step3 == "Yellow" or step3 == "yellow"):
#     print("Congratulations!!! You found the treasure")
# else:
#     print("You die🩻! Game over")