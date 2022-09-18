import blackjack_art
import random

logo = blackjack_art.logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand=[]
dealer_hand=[]
player_score=0
player_loses=False

def another_card(player_hand, player_score):
    if input("Type 'y' for another card, type 'n' to pass: ").lower() == "y":
        player_hand.append(random.choice(cards))
        player_score = sum(player_hand)

        print(player_score)
        if player_score > 21:
            count = 0
            for card in player_hand:
                if card == 11:
                    player_hand[count] = 1
                    print(player_hand)
                    player_score = sum(player_hand)
                count += 1
        print(f"Your current hand is: {player_hand}, current score: {player_score}")
        if player_score > 21:
            player_loses = True
        else:
            player_loses = False
        if player_loses != True:
            another_card(player_hand, player_score)

def blackjack():
        player_loses=False
        player_hand=[]
        dealer_hand=[]
        player_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))
        player_score = sum(player_hand)
        dealer_score = sum(dealer_hand)
        print(f"Your current hand is: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card is: {dealer_hand[0]}")
        another_card(player_hand, player_score)
        print(f"Dealer's hand is: {dealer_hand}, current score: {dealer_score}")
        if player_loses == False:
            while dealer_score < 17:
                dealer_hand.append(random.choice(cards))
                dealer_score = sum(dealer_hand)
                if dealer_score > 21:
                    count = 0
                    for card in dealer_hand:
                        if card == 11:
                            dealer_hand[count] = 1
                            print(dealer_hand)
                            dealer_score = sum(dealer_hand)
                        count += 1
                print("Dealer draws")
                print(f"Dealer's hand is: {dealer_hand}, current score: {dealer_score}")

        if player_loses == True:
            print("You lose!")
        elif player_score > dealer_score or dealer_score > 21:
            print("You win!")
        elif player_score == dealer_score:
            print("It's a draw!")
        else:
            print(dealer_score)
            print("You lose!")

        if input("Do you want to play a game of Blackjack?").lower() == "y":
            blackjack()
        else:
            print("OK, maybe next time.")


if input("Do you want to play a game of Blackjack?").lower() == "y":
    print(logo)
    blackjack()

else:
    print("OK, maybe next time.")
