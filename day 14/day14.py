# Higher or lower

from random import choice
from data import data

def format_data(choose):
    account_name = choose["name"]
    account_desc = choose["description"]
    account_country = choose["country"]
    return f"Account Details: {account_name}, {account_desc}, {account_country}"

def answer_check(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    
correct = True

score = 0
choose_b = choice(data)

while correct:    
    correct_guess = True    
    while correct_guess:
        choose_a = choose_b
        choose_b = choice(data)

        if choose_a == choose_b:
            choose_b = choice(data)
            
        print(f"Compare A: {format_data(choose_a)}")
        print(f"Against B: {format_data(choose_b)}")
        guess = input("Guess which account has higher followers, 'A' or 'B': ").lower()
        
        a_follower_count = choose_a["follower_count"]
        b_follower_count = choose_b["follower_count"]
        
        if guess == "a" or guess == "b":
            is_correct = answer_check(guess, a_follower_count, b_follower_count)
            if is_correct:
                score += 1
                print(f"You're Right, your current score: {score}")
            else:
                print(f"You are wrong. your score: {score}")
                correct_guess = False
        else:
            print("Kindly choose the correct option")
        
    correct = False