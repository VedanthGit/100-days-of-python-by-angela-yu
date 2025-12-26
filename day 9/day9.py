# Silent Auction System
def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amt = bidding_dict[bidder]
        if bid_amt > highest_bid:
            highest_bid = bid_amt
            winner = bidder
            
    print(f"The winner is {winner} with a bid of {highest_bid}")
    
bidders = {}

more_bidders = True

while more_bidders:
    
    name= input("What is your name? ")
    bid_amount = int(input("How much do you want to bid? "))
    bidders[name] = bid_amount
    
    should_continue = input("Are there any more bidders? Type 'Yes' or 'No: ").lower()
    
    if should_continue == "no":
        more_bidders = False
        
        find_highest_bidder(bidders)
    if should_continue == "yes":
        print("\n" * 50)