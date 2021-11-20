from sys import stdin as input
# input = open("./1149.txt")
N = int(input.readline())
board = [list(map(int, input.readline().split())) for _ in range(N)]

for i in range(1, N):
    board[i][0] = min(board[i][0] + board[i-1][1], board[i][0] + board[i-1][2])
    board[i][1] = min(board[i][1] + board[i-1][0], board[i][1] + board[i-1][2])
    board[i][2] = min(board[i][2] + board[i-1][0], board[i][2] + board[i-1][1])
    
print(min(board[-1]))