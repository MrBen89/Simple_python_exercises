import silentauc_art
from os import system, name

logo = silentauc_art.logo

bid_list = {}

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
running = True
while running == True:

    print(logo)

    name = input("Please enter your name: ")
    bid = int(input("please enter your bid: £ "))

    bid_list[name] = bid

    status = input("Are there any other bidders?").lower()
    clear()
    if status != "yes":
        running = False


winner = ""
high_bid = 0
for key in bid_list:
    if bid_list[key] > high_bid:
        high_bid = bid_list[key]
        winner = key

print(f"{winner} is the winner of the auction at £{high_bid}. Congratulations!")
