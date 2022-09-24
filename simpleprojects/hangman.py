import random
import hangman_words
import hangman_art
from os import system, name

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo

chosen_word = random.choice(word_list)

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(logo)
print(chosen_word)

lives = 6

display = []

for letter in chosen_word:
    display.append("_")

end_of_game = False
guessed = []

while not end_of_game:

    guess = input("Please guess a letter. ").lower()
    if guess not in guessed:
        guessed.append(guess)
        count = 0;
        hit = False
        for letter in chosen_word:
            if guess == letter:
                display[count] = letter
                count += 1
                hit = True
                clear()

            else:
                count += 1

        if hit == False:
            clear()
            print(f"Bad luck. The word didnt contain {guess}.")
            lives -= 1
    else:
        clear()
        print(f"You already guessed {guess}. Please try a  different letter.")
        print("Letters guessed;")
        print(guessed)


    print(display)
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You died!")
