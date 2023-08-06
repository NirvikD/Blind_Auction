import os
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidder in bidder_details:
        bidding_price = bidder_details[bidder]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidder
    print(f"The winner is {winner} with a bidding price of {highest_bid}")
bidder_data={}
end = False
while not end:
    name = input("What is your name ?: ")
    price = int(input("Enter the bid: "))
    bidder_data[name]=price
    more = int(input('''Are there more bidders: 
                        1.Yes 
                        2. No '''))
    if more ==2:
        end = True
        find_winner(bidder_data)
    elif more ==1:
        os.system('clear')
    else:
        print("Enter correct option")

