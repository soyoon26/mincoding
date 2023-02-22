from pprint import pprint

board = [list(map(int,input().split()))for i in range(5)]
# board = [[int(i) for i in input().split()] for _ in range(5)]
c_lst = [list(map(int,input().split())) for i in range(5)]
candidate = sum(c_lst,[])
b_cnt = 0

while b_cnt < 3:
    b_cnt = 0
    num = candidate.pop(0)
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0

    for_zero = []
    for_z = []
    for i in range(5):
        for_zero.append(board[i][i])
        for_z.append(board[i][4-i])
    if for_z.count(0) == 5:
        b_cnt += 1
    if for_zero.count(0) == 5:
        b_cnt += 1

    col_lst = list(map(list, zip(*board)))
    for i in range(5):
        if sum(board[i]) == 0:
            b_cnt += 1
        if sum(col_lst[i]) == 0:
            b_cnt += 1

pprint(num)


