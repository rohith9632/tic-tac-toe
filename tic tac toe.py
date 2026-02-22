
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
player = "X"
while True:
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    pos = int(input("Choose position (1-9): ")) - 1
    if board[pos] == "-":
        board[pos] = player
    else:
        print("Already taken! Try again.")
        continue
    if (board[0]==board[1]==board[2]==player or
        board[3]==board[4]==board[5]==player or
        board[6]==board[7]==board[8]==player or
        board[0]==board[3]==board[6]==player or
        board[1]==board[4]==board[7]==player or
        board[2]==board[5]==board[8]==player or
        board[0]==board[4]==board[8]==player or
        board[2]==board[4]==board[6]==player):  
        print("Player", player, "wins!")
        break
    if "-" not in board:
        print("It's a draw!")
        break
    if player == "X":
        player = "O"
    else:
        player = "X"