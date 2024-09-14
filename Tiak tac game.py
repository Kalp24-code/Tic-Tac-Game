def print_board(board):
    """Print the Tic Tac Toe board."""
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")


def check_winner(board, player):
    """Check if a player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
            all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False


def is_full(board):
    """Check if the board is full."""
    return all(cell != " " for row in board for cell in row)


def play_game():
    """Play the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("Cell already taken, try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
# if _name_ == "_main_":
#     play_game()
