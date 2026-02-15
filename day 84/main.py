def print_board(board):
    print("\nCurrent Board: ")
    for i in range(3):
        print(" " + " | ".join(board[i]))
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row col): ").strip()
            row, col = map(int, move.split())
            if row not in range(1, 4) or col not in range(1, 4):
                raise ValueError
            return row - 1, col - 1
        except ValueError:
            print(
                "Invalid input. Enter row and column as numbers from 1 to 3 (e.g., 2 3)."
            )


def main():
    print("=== TIC TAC TOE ===")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)
            row, col = get_move(current_player)

            if board[row][col] != " ":
                print("Cell already occupied. Choose another move.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins! 🎉")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw. Well played.")
                break

            current_player = "O" if current_player == "X" else "X"

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != "y":
            print("Game over. Thanks for playing.")
            break


if __name__ == "__main__":
    main()
