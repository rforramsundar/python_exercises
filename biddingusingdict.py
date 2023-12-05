
bidder_details = {}

loop_continue = True
while (loop_continue):
  bidder_name = input("Enter your name\n")
  bid_amount = int(input("What is your bid?\n"))
  another_bidder = input ("Are there any other bidders? Type 'yes' or 'no'\n")
  bidder_details[bidder_name] = bid_amount 
  if (another_bidder == 'no'):
    loop_continue = False

highest_bidder = ""
highest_amount = 0
print(bidder_details) 
for each_bidder in bidder_details:
  get_bid_amount = bidder_details[each_bidder]
  if (get_bid_amount > highest_amount):
    highest_amount = get_bid_amount
    highest_bidder = each_bidder

print(f"Highest bidder is {highest_bidder}")
