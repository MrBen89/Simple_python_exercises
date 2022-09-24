import random

choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors"))
AIchoice = random.randint(0,2)

if choice == 0:
    if AIchoice == 0:
        print("We both chose rock. It's a draw")
    elif AIchoice == 1:
        print("You chose rock, I chose paper. You lose!")
    else:
        print("You chose rock, I chose scissors. You win!")
elif choice == 1:
    if AIchoice == 0:
        print("You chose paper, I chose rock. You win!")
    elif AIchoice == 1:
        print("We both chose paper. It's a draw!")
    else:
        print("You chose paper, I chose scissors. You lose!")
elif choice == 2:
    if AIchoice == 0:
        print("You chose scissors, I chose rock. You lose!")
    elif AIchoice == 1:
        print("You chose scissors. I chose paper. You win!!")
    else:
        print("We both chose scissors. It's a draw!")
else:
    print("I'm sorry, I don't recognise that input")
