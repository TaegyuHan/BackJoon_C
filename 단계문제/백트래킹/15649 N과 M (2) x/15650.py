import sys

sys.stdin = open('./15650.txt')
N, M = map(int, sys.stdin.readline().split())


def backtracking(N, M, data_list, print_list):
  
    if M == 0:
        print(' '.join(map(str, print_list)))
        return

    for i in data_list:
        tmp_list = data_list.copy()
        p_tmp_list = print_list.copy()
        p_tmp_list.append(tmp_list[tmp_list.index(i)])
        tmp_list.remove(i)
        backtracking(N, M-1, tmp_list, p_tmp_list)


data_list = [i for i in range(1, N+1)]
backtracking(N, M, data_list, [])