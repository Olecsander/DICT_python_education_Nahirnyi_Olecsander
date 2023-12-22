"""Game: fascinating, educational"""

def print_board(board):
    print("---------")
    for row in board:
        print("|", " ".join(row), "|")
    print("---------")

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    return all(cell != "_" for row in board for cell in row)

def play_tic_tac_toe():
    board = [["_"] * 3 for _ in range(3)]
    current_player = "X"
    print_board(board)

    while True:
        try:
            x, y = map(int, input("Enter the coordinates: ").split())
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Coordinates should be from 1 to 3!")
                continue
            if board[x-1][y-1] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            board[x-1][y-1] = current_player
            print_board(board)
            if check_win(board, current_player):
                print(f"{current_player} wins")
                break
            if is_draw(board):
                print("Draw")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("You should enter numbers!")

play_tic_tac_toe()
