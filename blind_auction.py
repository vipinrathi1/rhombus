

print("Welcome to the secret auction program.")
bid = "yes"
bidders = {}
while bid == "yes":
    name = input("What is your name?: ")
    amount = int(input("What is the amount?: $"))
    bidders[name] = amount
    bid = input("Do you want to bid again? 'yes' or 'no'").lower()
if bid == "no":
    highest_bid = 0
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bid = bidders[bidder]
            highest_bidder = bidder

    print(f"{highest_bidder} won with a bid of ${highest_bid}")







