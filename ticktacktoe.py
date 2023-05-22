def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def play_game():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)

        print(f"Player {current_player}'s turn.")
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player

            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                game_over = True
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

play_game()
