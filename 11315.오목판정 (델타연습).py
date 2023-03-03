T = int(input())
for tc in range(T):
    N = int(input())
    board = [[i for i in input()] for i in range(N)]
    di = [0,1,1,1]
    dj = [1,-1,0,1]
    ans = "NO"
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for k in range(4):
                    cnt = 1
                    dx = i + di[k]
                    dy = j + dj[k]
                    if 0 <= dx < N and 0 <= dy < N:
                        if board[dx][dy] == 'o':
                            for l in range(1,5):
                                lx = i + di[k]*l
                                ly = j + dj[k]*l
                                if 0 <= lx < N and 0 <= ly < N:
                                    if board[lx][ly] == 'o':
                                        cnt += 1
                                        if cnt >= 5:
                                            ans = "YES"
                                    else :
                                        cnt = 0
    print(f"#{tc+1}",ans)
