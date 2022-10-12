
score_board = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: ""}
def print_board():
    top_row = f" {score_board[1]} | {score_board[2]} | {score_board[3]} "
    mid_row = f" {score_board[4]} | {score_board[5]} | {score_board[6]} "
    bot_row = f" {score_board[7]} | {score_board[8]} | {score_board[9]} "
    line_break = "- - - - - - "
    board_state = f"{top_row}\n{line_break}\n{mid_row}\n{line_break}\n{bot_row}"
    print(board_state)

def check_win(player):
    if score_board[1] == player and score_board[2] == player and score_board[3] == player:
        return player
    elif score_board[4] == player and score_board[5] == player and score_board[6] == player:
        return player
    elif score_board[7] == player and score_board[8] == player and score_board[9] == player:
        return player
    elif score_board[1] == player and score_board[4] == player and score_board[7] == player:
        return player
    elif score_board[2] == player and score_board[5] == player and score_board[8] == player:
        return player
    elif score_board[4] == player and score_board[6] == player and score_board[9] == player:
        return player
    elif score_board[1] == player and score_board[5] == player and score_board[9] == player:
        return player
    elif score_board[3] == player and score_board[5] == player and score_board[7] == player:
        return player

def ai_move():
    if score_board[5] == "":
        return 5
    # Check for winning plays
    elif (score_board[1] == "O" and score_board[2] == "O") or (score_board[6] == "O" and score_board[9] == "O") or (score_board[5] == "O" and score_board[7] == "O"):
        return 3
    elif (score_board[1] == "O" and score_board[3] == "O") or (score_board[5] == "O" and score_board[8] == "O"):
        return 2
    elif (score_board[3] == "O" and score_board[2] == "O") or (score_board[4] == "O" and score_board[7] == "O") or (score_board[5] == "O" and score_board[9] == "O"):
        return 1
    elif (score_board[5] == "O" and score_board[6] == "O") or (score_board[1] == "O" and score_board[7] == "O"):
        return 4
    elif (score_board[5] == "O" and score_board[4] == "O") or (score_board[3] == "O" and score_board[9] == "O"):
        return 6
    elif (score_board[1] == "O" and score_board[4] == "O") or (score_board[8] == "O" and score_board[9] == "O") or (score_board[5] == "O" and score_board[3] == "O"):
        return 7
    elif (score_board[7] == "O" and score_board[9] == "O") or (score_board[5] == "O" and score_board[2] == "O"):
        return 8
    elif (score_board[7] == "O" and score_board[8] == "O") or (score_board[3] == "O" and score_board[6] == "O") or (score_board[5] == "O" and score_board[1] == "O"):
        return 9
    # Check for blocking plays (could combine with above)
    elif (score_board[1] == "X" and score_board[2] == "X") or (score_board[6] == "X" and score_board[9] == "X") or (score_board[5] == "X" and score_board[7] == "X"):
        return 3
    elif (score_board[1] == "X" and score_board[3] == "X") or (score_board[5] == "X" and score_board[8] == "X"):
        return 2
    elif (score_board[3] == "X" and score_board[2] == "X") or (score_board[4] == "X" and score_board[7] == "X") or (score_board[5] == "X" and score_board[9] == "X"):
        return 1
    elif (score_board[5] == "X" and score_board[6] == "X") or (score_board[1] == "X" and score_board[7] == "X"):
        return 4
    elif (score_board[5] == "X" and score_board[4] == "X") or (score_board[3] == "X" and score_board[9] == "X"):
        return 6
    elif (score_board[1] == "X" and score_board[4] == "X") or (score_board[8] == "X" and score_board[9] == "X") or (score_board[5] == "X" and score_board[3] == "X"):
        return 7
    elif (score_board[7] == "X" and score_board[9] == "X") or (score_board[5] == "X" and score_board[2] == "X"):
        return 8
    elif (score_board[7] == "X" and score_board[8] == "X") or (score_board[3] == "X" and score_board[6] == "X") or (score_board[5] == "X" and score_board[1] == "X"):
        return 9
    #Check for empty corners
    elif score_board[1] == "":
        return 1
    elif score_board[3] == "":
        return 3
    elif score_board[7] == "":
        return 7
    elif score_board[9] == "":
        return 9
    # Check for empty sides
    elif score_board[2] == "":
        return 2
    elif score_board[4] == "":
        return 4
    elif score_board[6] == "":
        return 6
    elif score_board[8] == "":
        return 8

def main():
    game_running = True
    player = "X"
    print_board()
    while game_running == True:
        if player == "X":
            choice = int(input("Choose a space 1-9: "))
            if score_board[choice] == "":
                score_board.update({choice : player})
                print_board()
                if(check_win(player)):
                    game_running = False
                    print(f"{player} Wins!")
                player = "O"
            else:
                 print("Choose a different spot")
        else:
            print(")'s move...'")
            score_board[ai_move()] = "O"
            print_board()
            if(check_win(player)):
                game_running = False
                print(f"{player} Wins!")
            player = "X"


main()
