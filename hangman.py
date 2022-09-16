import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

display = []

for letter in chosen_word:
    display.append("_")

end_of_game = false

while not end_of_game:
    guess = input("Please guess a letter. ").lower()

    count = 0;
    for letter in chosen_word:
        if guess == letter:
            display[count] = letter
            count += 1

        else:
            count += 1

    print(display)
    if "_" not in display:
        end_of_game = true

print("You win!")
