import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print(chosen_word)

lives = 6

display = []

for letter in chosen_word:
    display.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Please guess a letter. ").lower()

    count = 0;
    hit = False
    for letter in chosen_word:
        if guess == letter:
            display[count] = letter
            count += 1
            hit = True

        else:
            count += 1

    if hit == False:
        lives -= 1

    print(display)
    print(stages[lives])
    if "_" not in display:
        end_of_game = True
        print("You win!")
    if lives == 0:
        end_of_game = True
        print("You died!")
