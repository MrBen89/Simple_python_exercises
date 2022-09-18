import higher_lower_art
import higher_lower_data
import random


logo = higher_lower_art.logo
vs = higher_lower_art.vs
data = higher_lower_data.data
score = 0
gameloop = True

compare_A = random.choice(higher_lower_data.data)
A_name = compare_A.get("name")
A_followers = compare_A.get("follower_count")
A_description = compare_A.get("description")
A_country = compare_A.get("country")


print(logo)
while gameloop == True:
    compare_B = random.choice(higher_lower_data.data)
    B_name = compare_B.get("name")
    B_followers = compare_B.get("follower_count")
    B_description = compare_B.get("description")
    B_country = compare_B.get("country")
    print(f"Compare A: {A_name}, a {A_description}, from {A_country}")
    print(vs)
    print(f"Against B: {B_name}, a {B_description}, from {B_country}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    if choice == "B" :
        if B_followers > A_followers:
            score += 1
            print(f"You're right! Current score: {score}.")
            compare_A = compare_B
            A_name = B_name
            A_followers = B_followers
            A_description = B_description
            A_country = B_country
        else:
            print(f"You lose. Score was {score}")
            again = input("Would you like to play again? Type 'Y' or 'N': ").upper()
            if again == "Y":
                compare_A = random.choice(higher_lower_data.data)
                A_name = compare_A.get("name")
                A_followers = compare_A.get("follower_count")
                A_description = compare_A.get("description")
                A_country = compare_A.get("country")
                score = 0
            else:
                print("Thanks for playing")
                gameloop = False
    elif choice == "A":
        if B_followers < A_followers:
            score += 1
            print(score)
        else:
            print(f"You lose. Score was {score}")
            again = input("Would you like to play again? Type 'Y' or 'N': ").upper()
            if again == "Y":
                compare_A = random.choice(higher_lower_data.data)
                A_name = compare_A.get("name")
                A_followers = compare_A.get("follower_count")
                A_description = compare_A.get("description")
                A_country = compare_A.get("country")
                score = 0
            else:
                print("Thanks for playing")
                gameloop = False
