from sys import stdin as input

# input = open("./1343.txt")
board = input.readline()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)