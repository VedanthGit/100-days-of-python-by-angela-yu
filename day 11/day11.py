# Blackjack Game
# Add up your cards to the largest number but lower or equal to 21, if you move over 21 you lose
import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "It's a Draw!!!"
    elif dealer_score == 0:
        return "You lose, dealer has blackjack"
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "Dealer wins! you went over 21"
    elif dealer_score > 21:
        return "You wins! dealer went over 21"
    elif dealer_score > user_score:
        return "Dealer Wins!!!"
    else:
        return "User wins!!!"

game = input("Do you want to play the game? Type 'y' or 'n': ").lower()

if game == "y":
    print("-------------------- GAME START --------------------")
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_cards(user_cards) 
        dealer_score = calculate_cards(dealer_cards)

        print(f"User Cards: {user_cards} | User score: {user_score}")
        print(f"Dealer First Card: {dealer_cards[0]} | Dealer score: {dealer_score}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if continue_game == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_cards(dealer_cards)
        
    
    print("\n--- Final Results ---")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))
    