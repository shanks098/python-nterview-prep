board = [" "]*9
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-+----+-")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-+----+-")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def check_draw():
    return " " not in board
current_player = "X"
print("Welcome to Tic-Tac-Toe!")
print()
print("Positions are numbered as follows:")
print("0 |1 |2 ")
print("-+----+-")
print("3 |4 |5 ")
print("-+----+-")
print("6 |7 |8 ")
while True:
    display_board()
    try:
        position = int(input(f"Player {current_player}, enter your move (0-8): "))
        if board[position] != " ":
            print("Position already taken. Try again.")
            continue
        if position < 0 or position > 8:
            print("Invalid position. Try again.")
            continue
        board[position] = current_player
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        if check_draw():
            display_board()
            print("It's a draw!")
            break
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")