import random

def checker():
    global guess
    global chosen_number
    if guess == chosen_number:
        return(f"You got it! The answer was {chosen_number}")
    elif guess < chosen_number:
        return("Too low. Guess again")
    elif guess > chosen_number:
        return("Too high. Guess again")
    else:
        return("Something went wrong")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
chosen_number = random.randrange(100)+1

if difficulty == "easy":
    lives = 10
else:
    lives = 5

while lives > 0:
    print(f"You have {lives} attempts remaining.")
    guess = int(input("Make a guess: "))
    print(checker())
    if checker() != (f"You got it! The answer was {chosen_number}"):
        lives -= 1
        if lives == 0:
            print("Out of lives, too bad!")
    else:
        lives = 0
