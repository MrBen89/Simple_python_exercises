
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

def main():
    game_running = True
    player = "X"
    print_board()
    while game_running == True:
        choice = int(input("Choose a space 1-9"))
        if score_board[choice] == "":
            score_board.update({choice : player})
            print_board()
            if(check_win(player)):
                game_running = False
                print(f"{player} Wins!")
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
             print("Choose a different spot")

main()
