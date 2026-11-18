#tic tac toe
def show(board):
    for row in range(3):
        print(" " + " | ".join(board[row * 3: row * 3 + 3]))
        if row < 2:
            print("---+---+---")

def winner(board):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] in "XO":
            return board[a]
    return None

def tic_tac_toe():
    board = [str(i) for i in range(1, 10)]
    player = "X"
    for turn in range(9):
        show(board)
        move = int(input(f"Player {player}, pick a square 1-9: ")) - 1
        while board[move] in "XO":
            move = int(input("Taken! Pick another: ")) - 1
        board[move] = player
        if winner(board):
            show(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    show(board)
    print("Draw!")
tic_tac_toe()