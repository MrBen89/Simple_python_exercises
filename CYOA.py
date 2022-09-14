print("Welcome to treasure Island")
print("You arrive at a dusty old crossroads, surrounded by gnarled trees. Which way will you go?")
input1 = input("Left or Right?")
if input1.lower == "l" or input1.lower() == "left":
    print("Moving forward, you arrive at a huge lake. The waters are dark and grimm.")
    print("In the distance you think you can see a building on an island.")
    print("What will you do next?")
    input2 = input("Swim across or wait for a boat?").lower()
    if input2 == "wait" or input2 == "wait for a boat":
        print("After waiting some time, you are finally taken across the island by a small boat, captained by a neon pink skeleton")
        print("After disembarking, you find the house you could see from the shore. There are three doors. Which shall you enter?")
        input3 = input("The red door. The green door. The neon pink door").lower()
        if input3 == "pink" or input3 == "neon pink" or input3 == "the neon pink door" or input3 == "pink door" or input3 == "neon pink door":
            print("Opening the door leads to a silent Disco, filled with treasures beyond your wildest dreams.")
            print("Congratulations, you win!")
        else:
            print("Unfortunately, behind the door was a manticore who eats your face. Game Over.")
    else:
        print("Unfortunately whilst trying to traverse the dank waters, you are eaten by a Kraken. Game Over.")
else:
    print("You walk into a clearing and are immediately eaten by a gnoll. Game Over.")
