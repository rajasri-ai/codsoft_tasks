import math

HUMAN = "X"
AI = "O"
EMPTY = " "


def print_board(board):
    print()
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True


def minimax(board, depth, is_max):
    winner = check_winner(board)

    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if is_full(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best = min(best, score)
        return best


def ai_move(board):
    best_score = -math.inf
    move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, 0, False)
                board[i][j] = EMPTY

                if score > best_score:
                    best_score = score
                    move = (i, j)

    board[move[0]][move[1]] = AI


def human_move(board):
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    break
                else:
                    print("Cell already occupied!")
            else:
                print("Invalid position!")
        except ValueError:
            print("Enter numbers only!")


def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]

    print("=== Tic-Tac-Toe AI ===")
    print("You are X")
    print("AI is O")

    while True:
        print_board(board)

        human_move(board)

        if check_winner(board) == HUMAN:
            print_board(board)
            print("You Win!")
            break

        if is_full(board):
            print_board(board)
            print("It's a Draw!")
            break

        ai_move(board)

        if check_winner(board) == AI:
            print_board(board)
            print("AI Wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a Draw!")
            break


if __name__ == "__main__":
    main()