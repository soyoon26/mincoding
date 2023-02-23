from pprint import pprint
N, M = map(int,input().split()) #행 열
K = int(input()) #화력
board = []
for i in range(N):
    board.append(list(input()))

di = [0,0,1,-1] #위아래
dj = [-1,1,0,0] #좌우

si = []
sj = []
for i in range(N):  # 폭탄지점 구하기
    for j in range(M):
        if board[i][j] == '@':
            si.append(i)
            sj.append(j)
dx_lst = []
dy_lst = []

for i in range(len(si)):
    for k in range(4):
        dx = si[i] + di[k]
        dy = sj[i] + dj[k]   #시작지점 상하좌우 탐색
        if 0 <= dx < N and 0 <= dy < M:   #범위
            if board[dx][dy] == '_' :  #방문하지 않고 길이 열려있다면
                dx_lst.append(dx)   #갈 수 있는 상하 dx_lst에 넣기
                dy_lst.append(dy)   #갈 수 있는 좌우 dy_lst에 넣기
                board[dx][dy] = '%'  #갈 수 있는 좌표 %표시

for i in range(N):
    for j in range(M):
        if board[i][j] == '%':
            if 0 <= i+1 < N:
                if board[i+1][j] == '@': #아래쪽이 @이면 이전에 위로 이동해준게 됨
                    for k in range(1,K):
                        if 0 <= i-k < N :
                            if board[i-k][j] == '_':
                                board[i-k][j] = '%'
            if 0 <= i - 1 < N:
                if board[i-1][j] == '@': #윗쪽이 @이면 이전 동작이 아래로 이동
                    for k in range(1,K):
                        if 0 <= i+k < N :
                            if board[i+k][j] == '_':
                                board[i+k][j] = '%'
            if 0 <= j - 1 < M:
                if board[i][j-1] == '@':  #왼쪽이 폭탄이면 나는 오른쪽으로 이동 중
                    for k in range(1,K):
                        if 0 <= j+k < M:
                            if board[i][j+k] == '_':
                                board[i][j+k] = '%'
            if 0 <= j + 1 < M:
                if board[i][j+1] == '@':
                    for k in range(1,K):
                        if 0 <= j-k < M:
                            if board[i][j-k] == '_':
                                board[i][j-k] = '%'

for i in range(N):
    for j in range(M):
        if board[i][j] == '@':
            board[i][j] = '%'

for i in range(N):
    print(''.join(board[i]))