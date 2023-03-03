from pprint import pprint
board = [[int(i) for i in input().split()] for _ in range(19)]

di = [0,1,1,1]
dj = [1,1,0,-1]
flag = 0
ans = 0
ans_i = 0
ans_j = 0

for i in range(19):
    for j in range(19):
        if board[i][j] :
            n= board[i][j]
            for k in range(4):
                cnt = 1
                for l in range(1,5):
                    dx = i + di[k]*l
                    dy = j + dj[k]*l
                    if 0 <= dx < 19 and 0 <= dy < 19:
                        if board[dx][dy] == n:
                            cnt += 1
                        if cnt == 5:
                            flag = 1
                            ans = n
                            if j > dy :
                                ans_i = dx + 1
                                ans_j = dy + 1
                            else :
                                ans_i = i + 1
                                ans_j = j + 1
                            if 0 <= dx + di[k] < 19 and 0 <= dy + dj[k] < 19:
                                if board[dx+di[k]][dy+dj[k]] == n:
                                    flag = 0
                                    ans = 0
                                    ans_i = 0
                                    ans_j = 0
                            if 0 <= i - di[k] < 19 and 0 <= j - dj[k] < 19:
                                if board[i - di[k]][j - dj[k]] == n:
                                    flag = 0
                                    ans = 0
                                    ans_i = 0
                                    ans_j = 0
                if flag == 1:
                    break
        if flag == 1:
            break
    if flag == 1:
        break


if ans_i != 0 and ans_j != 0:
    print(ans)
    print(ans_i,ans_j)
else:
    print(ans)